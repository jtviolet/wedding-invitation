# Wedding Invitation

This Python application aids in automating wedding invitations using Python, AirTable, and Twilio. This Python script is only 1/3 of the puzzle. You will also need to make a copy of this AirTable base: https://airtable.com/shrInjQfyQVwbRHHi and you will need to learn how to create a Flow in Twilio to handle your data. I will be posting more about my Twilio flow soon.

This script will pull all of your guests from your AirTable base and kick-off a Twilio flow for each guest. Learn how to set it up below.
## Getting Started

### Environment Variables
You will need to set a few environment variables first.

 * `TWILIO_ACCOUNT_SID` - Twilio account sid, can be found [on your Twilio console](https://www.twilio.com/console).
 * `TWILIO_AUTH_TOKEN` - Twilio auth token, also found [on your Twilio console](https://www.twilio.com/console).
 * `TWILIO_PHONE_NUMBER` - The Twilio phone number you want to use to send the invitations from.
 * `TWILIO_WEDDING_FLOW_ID` - The Flow ID of your wedding invitation flow.
 * `AIRTABLE_API_KEY` - Your AirTable API key, can be found [in your AirTable account](https://airtable.com/account).
 * `AIRTABLE_BASE_ID` - The base ID of your wedding invitations base. [You can find your base ID here](https://airtable.com/api).
 * `AIRTABLE_TABLE_NAME` - The name of the table in your base where you store your guest list.d
### Prerequisites
Before you run this script, you will first need to have done a few things:

 1. Create an account on Twilio and get a phone number
 2. Create a flow on Twilio [here](https://www.twilio.com/console/studio/flows). I will be writing a tutorial on this soon, but for now here is a [screenshot of my flow](https://jade-bat-5280.twil.io/assets/twilio%20wedding%20flow.png).
 3. Create an AirTable account and make a copy of [this AirTable base](https://airtable.com/shrInjQfyQVwbRHHi).

### Installing
Once you have your environment variables set and the above prerequisites done, you'll only need to run:

```
python app.py
```

## Contributing

Feel free to submit a pull request.


## License

This project is licensed under the MIT License - see the LICENSE file for details.