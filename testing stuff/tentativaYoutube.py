import httplib2
import os
import sys

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow


CLIENT_SECRETS_FILE = "client_secrets.json"
API_KEY = "AIzaSyCkwKbt6WlZHSw7xV18xxwfkT-OZeDnwXc"

youtube = build('youtube', 'v3' , developerKey = API_KEY)

query = input("aAAAA pesquisa pl0x: ")

res = youtube.search().list(q = query, part = 'snippet', type = 'video')
result = res.execute()

for search_result in result.get("items", []):
    print ("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["videoId"]))