
import requests
import json
import os
from dotenv import load_dotenv
import threading
import re
from twilio.rest import Client

load_dotenv()
GROUPME_API_KEY = os.environ.get("GROUPME_API_KEY", "Need enviornment variable GROUPME_API_KEY")
GROUP_ID = os.environ.get("GROUP_ID", "Need environment variable GROUP_ID")
TWILIO_SID = os.environ.get("TWILIO_SID","Need environment variable TWILIO_ID")
AUTH_TOKEN = os.environ.get("AUTH_TOKEN", "Need environment variable AUTH_TOKEN (twilio auth token)")
TO_NUMBER = os.environ.get("TO_NUMBER", "Need environment variable TO_NUMBER (your phone number)")
FROM_NUMBER = os.environ.get("FROM_NUMBER", "Need environmnet variable FROM_NUMBER (Twilio phone number)")

user_id = 28092669
#"Test" group is is 59490587

def message_group(message, group_id, API_KEY):
    url = f"https://api.groupme.com/v3/groups/{group_id}/messages?token={API_KEY}"
    jsonMessage = {"message":{"guid" : "86db84c3-422b-48cf-9c4c-b43ed7988efa", "text" : f"{message}"}}
    response = requests.post(url, json=jsonMessage)
    return response

def parse_response_thread(response, schedule):
    if(get_groupme_groupid(response) == GROUP_ID):
        text = get_groupme_text(response).lower()
        if ("can anyone" in text or ("looking" in text and "cover" in text)):
            time = re.search("\d+:\d+.*\d+:\d+", text)
            for key in schedule.keys():
                if(key in text):
                    if("".join(time.group().split()) in schedule[key]):
                        message_group(f"@{get_groupme_sender_name(response)} Yea I'll take it", GROUP_ID, GROUPME_API_KEY)
                        content = f"ShiftGrabber picked up shift on {key} from {time.group()}"
                        client.messages.create(to = TO_NUMBER, from_ = FROM_NUMBER, body = content)

def get_groupme_text(respone):
    return json.loads(response.text)[1]["data"]["subject"]["text"]

def get_groupme_groupid(response):
    return json.loads(response.text)[1]["data"]["subject"]["group_id"]

def get_groupme_sender_name(response):
    return json.loads(response.text)[1]['data']['subject']['name']

def setup_connection(id, url):
    id = 1
    body1 = {
            "id":f"{id}",
            "channel":"/meta/handshake",
            "successful":True,
            "version":"1.0",
            "supportedConnectionTypes":["long-polling","cross-origin-long-polling","callback-polling","websocket","in-process"],
            "clientId":"0wgyczg0sbd91m0uc8wyv09qblos",
            "advice": {"reconnect":"retry","interval":0,"timeout":30000}
        }
    
    response = requests.post(url, json=body1)
    print(response.status_code)
    client_id = json.loads(response.text)[0]["clientId"]
    id += 1
    body2 = {
        "channel":"/meta/subscribe",
        "clientId":f"{client_id}",
        "subscription":f"/user/{user_id}",
        "id":f"{id}",
        "ext":
          {
            "access_token":f"{GROUPME_API_KEY}",
            "timestamp":1322556419
          }
      }
    response = requests.post(url, json=body2)
    return client_id
          
def get_day(day):
    shifts = input("Please enter your availability for " + day + ": ")
    return shifts.split(", ")

def get_schedule():
    schedule = {}
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    for day in days:
        schedule[day.lower()] = get_day(day)
    return schedule


url = "https://push.groupme.com/faye"
print("Please enter your availability as a comma separated list  of 4 hour blocks in Military Time")
print("ie. if available from 8:00AM-12:00PM and 4:00PM-Midnight, enter '8:00-12:00, 16:00-20:00, 20:00-2400'")
user_schedule = get_schedule()

client = Client(TWILIO_SID, AUTH_TOKEN)

id = 0
client_id =setup_connection(id, url)
while True:
    try:
        body3 = {
        "channel":"/meta/connect",
        "clientId":f"{client_id}",
        "connectionType":"long-polling",
        "id":f"{id}"
        }
        response = requests.post(url, json=body3)
        print(response.status_code)
        parser = threading.Thread(target=parse_response_thread, args=(response, user_schedule))
        parser.start()
        id += 1
    except KeyboardInterrupt:
        break
    except:
        print("Reconnecting")
        client_id = setup_connection(id, url)        




