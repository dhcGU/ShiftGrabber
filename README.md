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

To access your groups and messages, there must be an environment variable "GROUPME_API_KEY" which stores a valid GroupMe API Key. [This tutorial](https://dev.groupme.com/tutorials/oauth) shows how to obtain one. Once you have an API key, you must use it to retrieve the group number of the group in which ShiftGrabber is to parse messages and pick up shifts. To obtain the group number, follow the directions in the [GroupMeAPI Reference](https://dev.groupme.com/docs/v3#groups).
