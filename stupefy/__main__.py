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
import sys



def get_playlist_tracks(username, playlist_id):
    #this function gets a user playlist, by the URI and returns the tracklist json object
    
    #gets at most 50 items on a playlsit, due to youtube quota impact
    results = spotify.user_playlist_tracks(username, playlist_id, limit=50)
    tracks = results['items']

    if results['total'] > 50 :
        answer = interface.print_quota_warning(results['total']) 
        
        if answer == "Y":
            return tracks
        else:
            interface.print_goodbye()
            return None

    #while results['next']:
        #results = spotify.next(results)
        #tracks.extend(results['items'])
    
    return tracks


def create_youtube_playlist(user_title, user_description):

    playlists_insert_response = youtube.playlists().insert(
        part="snippet,status",
        body=dict(
            
            snippet=dict(
                title=user_title,
                description=user_description
            ),

            status=dict(
                privacyStatus="private"
            )
        )
    ).execute()

    return playlists_insert_response["id"]


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

if tracks == None:
    sys.exit()

#gets information for the playlist and creates it
#FIXME: Login Required
user_title = input("Tell us what shall be thy playlist name: ")
user_description = input("I hate this as much as you do but you need to add a description: ")

playlist_id = create_youtube_playlist(user_title, user_description);


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

    #
    #gets only the first result, due to quota issues
    #res = youtube.search().list(q = query, part = 'snippet', type = 'video', maxResults=1);
    #result = res.execute()

    #for search_result in result.get("items", []):
        #print ("%s (%s)" % (search_result["snippet"]["title"], search_result["id"]["videoId"]))

    interface.print_goodbye()
    sys.exit