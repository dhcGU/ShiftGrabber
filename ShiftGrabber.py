from groupy import Client
from groupy.api import bots
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
GROUPME_API_KEY = os.environ.get("GROUPME_API_KEY", "Need enviornment variable GROUPME_API_KEY")
GROUP_ID = os.environ.get("GROUP_ID", "Need environment variable GROUP_ID")

user_id = 28092669
#"Test" group is is 59490587
groups = list(client.groups.list_all())
for group in groups:
    print(group.name)

def message_group(message, group_id, API_KEY):
    url = f"https://api.groupme.com/v3/groups/{group_id}/messages?token={API_KEY}"
    jsonMessage = {"message":{"guid" : "86db84c3-422b-48cf-9c4c-b43ed7988efa", "text" : f"{message}"}}
    response = requests.post(url, json=jsonMessage)
    return response


url = "https://push.groupme.com/faye"
body1 = {
        "id":"1",
        "channel":"/meta/handshake",
        "successful":True,
        "version":"1.0",
        "supportedConnectionTypes":["long-polling","cross-origin-long-polling","callback-polling","websocket","in-process"],
        "clientId":"0wgyczg0sbd91m0uc8wyv09qblos",
        "advice": {"reconnect":"retry","interval":0,"timeout":30000}
    }


body2 = {
    "channel":"/meta/subscribe",
    "clientId":"37413m11wuk0e0nngcny1p1mf570iyl9wi0",
    "subscription":"/user/28092669",
    "id":"2",
    "ext":
      {
        "access_token":f"{GROUPME_API_KEY}",
        "timestamp":1322556419
      }
  }
      
      
      
body3 = {
    "channel":"/meta/connect",
    "clientId":"37413m11wuk0e0nngcny1p1mf570iyl9wi0",
    "connectionType":"long-polling",
    "id":"4"
  }
id = 5      
while True:
    body3 = {
    "channel":"/meta/connect",
    "clientId":"37413m11wuk0e0nngcny1p1mf570iyl9wi0",
    "connectionType":"long-polling",
    "id":f"{id}"
    }
    response = requests.post(url, json=body3)
    print(response.status_code)
    id += 1





