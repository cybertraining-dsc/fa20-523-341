import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# API Tokens
clientID = '688f828e787d49768560dc3b01ad1527'
clientSecret = '1c92d4cff46546558e68bacdcb17a029'

credentialsManager = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=credentialsManager)

# Dictionary to assign track IDs to the track names, for easy lookup
tracks = {}

# get top 50 songs in 2020
track_results = sp.search(q='year:2020', type='track', limit=50, offset=1)

# populate tracks dictionary with track ids as keys, track names as values
for i, t in enumerate(track_results['tracks']['items']):
    tracks[t['id']] = t['name']
print(tracks)

# get audio data for each track in tracks
audio_data = sp.audio_features(tracks.keys())

# print track data
print(audio_data)
