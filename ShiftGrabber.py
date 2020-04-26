
import requests
import json
import os
from dotenv import load_dotenv
import threading
import re

load_dotenv()
GROUPME_API_KEY = os.environ.get("GROUPME_API_KEY", "Need enviornment variable GROUPME_API_KEY")
GROUP_ID = os.environ.get("GROUP_ID", "Need environment variable GROUP_ID")

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
        if ("can anyone" in text):
            time = re.search("\d+:\d+.*\d+:\d+", text)
            for key in schedule.keys():
                if(key in text):
                    if(time.group() in schedule[key]):
                        message_group("Yea I'll take it", GROUP_ID, GROUPME_API_KEY)
            
def get_groupme_text(respone):
    return json.loads(response.text)[1]["data"]["subject"]["text"]

def get_groupme_groupid(response):
    return json.loads(response.text)[1]["data"]["subject"]["group_id"]


user_schedule = {
        "monday" : ["16:00-20:00"],
        "tuesday" : [], 
        "wednesday" : [],
        "thursday" : [],
        "friday" : [],
        "saturday" : [],
        "sunday" : [],
        }

url = "https://push.groupme.com/faye"
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
while True:
    body3 = {
    "channel":"/meta/connect",
    "clientId":f"{client_id}",
    "connectionType":"long-polling",
    "id":f"{id}"
    }
    response = requests.post(url, json=body3)
    print(response.status_code)
    parser = threading.Thread(target=parse_response_thread, args=(response,user_schedule))
    parser.start()
    id += 1





