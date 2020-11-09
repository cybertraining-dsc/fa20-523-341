import re

import spotipy
import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords


def get_genius_url(title, artist):
    genius = 'https://api.genius.com/search'
    data = {'q': title + ' ' + artist}
    headers = {'Authorization': 'Bearer ' + 'O06q2KIQgwgP6G7nx9kUjnoOyM2hpVumE8jtFiJh8kD-CtW64l51mUeWeZeYf4LV'}
    response = requests.get(genius, data=data, headers=headers)
    song_url = ''
    for hit in response.json()['response']['hits']:
        if record['artist'] == hit['result']['primary_artist']['name']:
            song_url = hit['result']['url']
            print(hit['result']['primary_artist']['name'])
            break
    return song_url


def get_genius_lyrics_from_url(genius_url):
    lyrics = requests.get(genius_url)
    html = BeautifulSoup(lyrics.text, 'html.parser')
    genius_lyrics = html.find('div', class_='lyrics').get_text()
    return genius_lyrics


def lyrical_analysis(lyrics):
    return


def remove_stopwords(lyrics):
    lines = lyrics.split('\n')
    filtered = ""
    for line in lines:
        line = re.sub(r'[\(\[].*?[\)\]]', ' ', line)
        line = re.sub(r'\n', ' ', line)
        # line = re.sub(r'[\\+u.*)]', ' ', line)
        filtered += line
    lyrics_words = filtered.split(' ')
    stops = stopwords.words('english')
    removed_stopwords = [re.sub(r'[\\+u.*]', '', word) for word in lyrics_words if word not in stops and word != '']
    print(removed_stopwords)


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
    tracks[t['id']] = [t['name'], t['artists'][0]['name']]

# get audio data for each track in tracks
audio_data = sp.audio_features(tracks.keys())

for record in audio_data:
    record['name'] = tracks[record['id']][0]
    record['artist'] = tracks[record['id']][1]
    url = get_genius_url(record['name'], record['artist'])
    if url != '':
        lyrics = get_genius_lyrics_from_url(url)
        remove_stopwords(lyrics)

print(len(audio_data))
