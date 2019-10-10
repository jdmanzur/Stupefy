from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

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

uri = input("Insira uma uri válida de uma playlist do spotify:" )

username = ' '
playlist_id = uri.split(':')[2]

tracks = get_playlist_tracks(username, playlist_id)

for i, item in enumerate(tracks):
        track = item['track']
        print("   %d %s || %s" %(i, track['artists'][0]['name'],track['name']))