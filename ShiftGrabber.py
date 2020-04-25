from groupy import Client
from groupy.api import bots
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
GROUPME_API_KEY = os.environ.get("GROUPME_API_KEY", "Need enviornment variable GROUPME_API_KEY")
GROUP_ID = os.environ.get("GROUP_ID", "Need environment variable GROUP_ID")

client = Client.from_token("3ec4dfe0672501385dda422a9716c2d0")
#"Test" group is is 59490587
groups = list(client.groups.list_all())
for group in groups:
    print(group.name)
API_ENDPOINT = "https://api.groupme.com/v3/bots?token=3ec4dfe0672501385dda422a9716c2d0"

def message_group(message, group_id, API_KEY):
    url = f"https://api.groupme.com/v3/groups/{group_id}/messages?token={API_KEY}"
    jsonMessage = {"message":{"guid" : "86db84c3-422b-48cf-9c4c-b43ed7988efa", "text" : f"{message}"}}
    response = requests.post(url, json=jsonMessage)
    return response




response = message_group("testing", GROUP_ID, GROUPME_API_KEY)


print(response.status_code)