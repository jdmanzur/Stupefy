#!/usr/bin/env python

from oauth2client.client import flow_from_clientsecrets
from spotipy.oauth2 import SpotifyClientCredentials
from oauth2client.tools import argparser, run_flow
from apiclient.errors import HttpError
from apiclient.discovery import build
from oauth2client.file import Storage
from settings_config import config

import interface
import httplib2
import spotipy
import time
import json



def get_playlist_tracks(username, playlist_id):
    #this function gets a user playlist, by the URI and returns the tracklist json object
    
    results = spotify.user_playlist_tracks(username, playlist_id)
    tracks = results['items']

    while results['next']:
        results = spotify.next(results)
        tracks.extend(results['items'])
    return tracks



interface.print_welcome_message()

#AUTH spotify
#consegue autorização pelas credenciais cadastradas no My Application do Spotify
#não esquecer de passar como parâmetro o id do cliente e o secret id da appliacção
client_credentials_manager = SpotifyClientCredentials(client_id= config.SPCLIENT_ID, client_secret=config.SPCLIENT_SECRET)
spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
#AUTH youtube
youtube = build('youtube', 'v3' , developerKey = config.YTAPI_KEY)
################################################################


uri = input("Please, paste a valid Spotify URI: " )
#separates the playlist id from the rest of the URI
playlist_id = uri.split(':')[2]
#gets playlists tracks by using the function defined before
tracks = get_playlist_tracks('', playlist_id)

total = len(list(tracks))
#começa a printar a barrinha de progresso
interface.print_progress_bar(0, total, prefix = 'Progress:', suffix = 'Complete', length = 50)
#pesquisa no youtube os resultados do spotify
for i, item in enumerate(tracks):

    track = item['track']
    query = str(track['artists'][0]['name']) + ' ' + str(track['name'])
    
    time.sleep(0.1)
    #atualiza a barrinha de progresso
    interface.print_progress_bar(i + 1, total, prefix = 'Progress:', suffix = 'Complete', length = 50)

    #FIXME: quota stuff to search
    #res = youtube.search().list(q = query, part = 'snippet', type = 'video')
    #result = res.execute()

    #for search_result in result.get("items", []):
    #  print ("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["videoId"]))

