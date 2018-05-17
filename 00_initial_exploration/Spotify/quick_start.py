import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = '1ea8971ec11545499ac435640d4cf14e'
client_secret = 'dfc55156db2d4d1599f7d6f87562d4fb'
client_credentials_manager = spotipy.oauth2.SpotifyClientCredentials(client_id, client_secret)

spotify = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

name = 'rihanna'
result = spotify.search(q='artist:' + name, type='artist')
print(result)
