# Amazon Price Tracker Script
This script monitors the price of the user's desired product and sends the user a Whatsapp message when the price is reduced.


### Requirements
Install the following Python libraries:
1. pip3 install twilio
2. pip3 install requests
3. pip3 install bs4
4. pip3 install datetime


### Instructions
- Make sure the .py and .json files are placed in the same directory
- Head over to https://www.twilio.com/ and sign up for an account
- After you have verified your account, go to https://www.twilio.com/console/sms/whatsapp/learn and follow the instructions
   - You only need to do 'Step 1' by sending the displayed message to Twilio's Whatsapp
   - You can then leave the page. The following steps are absolutely not required to be done
- Now open 'auth.json' and fill in the required information
   - 'account_sid' and 'auth_token' can be found at https://www.twilio.com/console
- During trial period, you get £12 worth of credit for free
   - Yes, sending Whatsapp messages using Twilio API do cost money
   
 
 ### Troubleshooting
 I doubt anyone would receive blocked response but if you were unable to scrape the page content, try changing your user agent
 - This could be done by going to your browser and search for 'my user agent'
 - Copy the displayed string and replace the default headers dictionary in the .py file with that
