from twilio.rest import Client
import airtable as at
import requests
import json
import os

print("Retrieving Guest table records from AirTable...")
guest_table = at.Airtable(os.getenv('airtable_base_id'), os.getenv('airtable_table_name'), os.getenv('airtable_api_key'))

def main():
    # get guest table records
    guest_records = get_guest_list()

    # send invites to all guests
    print("Sending invitation to all guests...")
    for guest_record in guest_records:
        invite_guest(guest_record)


# grab the current guest list from AirTable
def get_guest_list():
    print("Guest table records retrieved...")
    return guest_table.get_all()


# send an invite to a given guest
def invite_guest(guest_record):
    twilio_client = Client(os.getenv('twilio_account_sid'), os.getenv('twilio_auth_token'))

    # send invites only to main guests, not plus-ones
    if 'is_plus_one' not in guest_record['fields']:
        print("Sending invitation to {}".format(guest_record['fields']['guest']))
        
        # send invite to guests without a plus-one
        if 'plus_one' not in guest_record['fields']:
            # send invite to user that doesn't have a plus-one
            execution = twilio_client.studio.flows(os.getenv('twilio_wedding_flow_id')).executions.create(
                            parameters={
                                'guest_name': guest_record['fields']['guest'].rsplit(' ', 1)[0],
                                'guest_record_id': guest_record['id']
                            },
                            to=guest_record['fields']['phone_number'],
                            from_=os.getenv('twilio_phone_number')
                        )
            save_guest_execution(guest_record['id'], execution.sid)

        # send invites to guests with plus-ones
        else:
            plusone_name = get_plusone_name(guest_record['fields']['plus_one'][0])

            execution = twilio_client.studio.flows(os.getenv('twilio_wedding_flow_id')).executions.create(
                            parameters={
                                'guest_name': guest_record['fields']['guest'].rsplit(' ', 1)[0],
                                'guest_record_id': guest_record['id'],
                                'plusone_name': plusone_name,
                                'plusone_record_id': guest_record['fields']['plus_one'][0]
                            },
                            to=guest_record['fields']['phone_number'],
                            from_=os.getenv('twilio_phone_number')
                        )
            save_guest_execution(guest_record['id'], execution.sid)


def save_guest_execution(guest_record_id, execution_sid):
    airtable_url = 'https://api.airtable.com/v0/{}/{}/{}'.format(os.getenv('airtable_base_id'), os.getenv('airtable_table_name'), guest_record_id)
    headers = {
        "Authorization": "Bearer {}".format(os.getenv('airtable_api_key')),
        "Content-Type": "application/json"
    }
    body = {
        "fields": {
            "twilio_execution_id": execution_sid
        }
    }
    
    requests.patch(airtable_url, headers=headers, data=json.dumps(body))


def get_plusone_name(plusone_record_id):
    plusone_record = guest_table.get(plusone_record_id)
    return plusone_record['fields']['guest'].rsplit(' ', 1)[0]


if __name__ == '__main__':
    main()