# ShiftGrabber

ShiftGrabber is designed to make pick up shifts from a work GroupMe for the user. This program was built to pick up shifts from a specific groupchat, so it has some conventions that may not be universally applicable (shifts are in military time, expects certain common phrases from users when discerning if a messsage is offering a shift, etc.) but it is possible to alter the program so that it functions for a specific user's purpose.

ShiftGrabber is a command line python program. To run this program, fork the repository and download it to your machine. <br>From a terminal/command line window configured with Python in your path, you can execute the program with the following command in the robo-advisor directory (adjust the slash accordingly depending on your operating system):
```
python ShiftGrabber.py
```

It requires the requests, os, json, dotenv, threading, re, and twilio packages. To install packages, run 
```
pip install -r requirements.txt
```

To access your groups and messages, there must be an environment variable "GROUPME_API_KEY" which stores a valid GroupMe API Key. [This tutorial](https://dev.groupme.com/tutorials/oauth) shows how to obtain one. Once you have an API key, you must use it to retrieve the group number of the group in which ShiftGrabber is to parse messages and pick up shifts. To obtain the group number, follow the directions in the [GroupMeAPI Reference](https://dev.groupme.com/docs/v3#groups). You will also need to obtain your user ID from the GroupMe API and store it in a USER_ID environment variable. You can make requests to their API via the requests package and unpack the json response to get these IDs. A get request to https://api.groupme.com/v3/groups/**YourAuthentificationToken** should send a response that contains groups with their IDs and members with their IDs. Parse the response to obtain the appropriate group number and your user ID. Once you have the group number, it must be stored in an environment variable named "GROUP_ID". You will also need a Twilio account account and credentials as described in [this](https://github.com/prof-rossetti/intro-to-python/blob/master/notes/python/packages/twilio.md) repo. Store your Twilio Account SID in an environment variable TWILIO_SID and the Authentification Token in another environment variable AUTH_TOKEN. Finally, you will need to store your phone number in a TO_NUMBER environment variable and your [Twilio phone number](https://www.twilio.com/console/sms/getting-started/build) in environmnet variable FROM_NUMBER.

ShiftGrabber prompts the user to enter their availability for each day in military time in 4 hour blocks as shifts in ShiftGrabber's GroupMe group are in this format. They must be in a comma separated list, so if the user is available from 12:00PM - 8:00PM on Monday, when prompted for Monday's availability the user will enter "12:00-16:00, 16:00-20:00". ShiftGrabber then parses all incoming messages from the group specified by GROUP_ID. If a message contains language indicating that its senders is seeking shift coverage, such as "Can anyone" and "cover", ShiftGrabber will send a response in the group that the user is wiling to cover the shift. It also sends the user a text message at the phone number specified by TO_NUMBER notifying them that SHiftGrabber has picked up a shift on their behalf. 
