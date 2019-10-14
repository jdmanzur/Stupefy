import httplib2
import os
import sys
import spotipy

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.file import Storage
from oauth2client.tools import argparser, run_flow
from spotipy.oauth2 import SpotifyClientCredentials

#PARTE SPOTIFY

def get_playlist_tracks(username,playlist_id):
    results = spotify.user_playlist_tracks(username,playlist_id)
    tracks = results['items']

    while results['next']:
        results = spotify.next(results)
        tracks.extend(results['items'])
    return tracks

#consegue autorização pelas credenciais cadastradas no My Application do Spotify
#não esquecer de passar como parâmetro o id do cliente e o secret id da appliacção
client_credentials_manager = SpotifyClientCredentials(client_id="cd23967850ec488ea054f39ba6ad5161", client_secret="5fe09923eda44e58a37d610fcc1d6bbe")
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#AUTH youtube
CLIENT_SECRETS_FILE = "client_secrets.json"
API_KEY = "AIzaSyCkwKbt6WlZHSw7xV18xxwfkT-OZeDnwXc"
youtube = build('youtube', 'v3' , developerKey = API_KEY)

################################################################


uri = input("Insira uma uri válida de uma playlist do spotify:" )

#TODO: ajeitar codigo abaixo depois para generalizar para qualquer URI
username = ' '
playlist_id = uri.split(':')[2]

tracks = get_playlist_tracks(username, playlist_id)


#pesquisa no youtube os resultados do spotify
for track in tracks.get("track", []):
    track = item['track']
    query = "" + track['artists']['name'] + ' ' + track['name']


    res = youtube.search().list(q = query, part = 'snippet', type = 'video')
    result = res.execute()

    for search_result in result.get("items", []):
        print ("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["videoId"]))

    