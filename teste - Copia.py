from spotipy.oauth2 import SpotifyClientCredentials
import spotipy


#consegue autorização pelas credenciais cadastradas no My Application do Spotify
#não esquecer de passar como parâmetro o id do cliente e o secret id da appliacção
client_credentials_manager = SpotifyClientCredentials(client_id="cd23967850ec488ea054f39ba6ad5161", client_secret="5fe09923eda44e58a37d610fcc1d6bbe")
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

uri = input("Entre uma uri válida de uma playlist do spotify:" )

username = ' '
playlist_id = uri.split(':')[2]

results = sp.user_playlist(username, playlist_id, fields="tracks")

tracks = results['tracks']

for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %s || %s" % (i, track['artists'][0]['name'],track['name']))