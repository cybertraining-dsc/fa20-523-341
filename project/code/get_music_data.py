import csv
import os
import re

import spotipy
import requests
from bs4 import BeautifulSoup
from spotipy.oauth2 import SpotifyClientCredentials
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords

nltk.download('vader_lexicon')
nltk.download('stopwords')


def get_genius_url(title, artist):
    genius = 'https://api.genius.com/search'
    data = {'q': title + ' ' + artist}
    headers = {'Authorization': 'Bearer ' + 'O-txEXzcRqwinpQX3P5AMzLRka8sq1HwBfZFBlSGCdaDZa14P4uXyeSKbgTCvARM'}
    response = requests.get(genius, data=data, headers=headers)
    song_url = ''
    for hit in response.json()['response']['hits']:
        if artist == hit['result']['primary_artist']['name']:
            # print(title + '|' + artist)
            song_url = hit['result']['url']
            break
    return song_url


def get_genius_lyrics_from_url(genius_url):
    lyrics = requests.get(genius_url)
    html = BeautifulSoup(lyrics.text, 'html.parser')
    genius_lyrics = html.find('div', class_='lyrics').get_text()
    return genius_lyrics


def lyrical_analysis(song_lyrics):
    lines = re.split(r'\n', song_lyrics)
    filtered = ""
    for line in lines:
        line = re.sub(r'[\(\[].*?[\)\]]|\n|\u2005|\u205f', '', line)
        filtered += line + '\n'
    cleaned_lyrics = os.linesep.join([line for line in filtered.splitlines() if line])
    sia = SentimentIntensityAnalyzer()
    senti_data = {}
    positive = 0
    negative = 0
    neutral = 0
    for line in cleaned_lyrics.split('\n'):
        line_sentiment = sia.polarity_scores(line)
        score = line_sentiment['compound']
        if score >= 0.5:
            positive += 1
        elif score < -0.1:
            negative += 1
        else:
            neutral += 1
    total = positive + neutral + negative
    senti_data['num_positive'] = positive
    senti_data['num_negative'] = negative
    senti_data['num_neutral'] = neutral
    senti_data['positivity'] = positive / total
    senti_data['negativity'] = negative / total
    senti_data['neutrality'] = neutral / total
    return senti_data


def count_unique_words(array_of_words):
    unique_words = []
    for word in array_of_words:
        if word not in unique_words:
            unique_words.append(word)
    return len(unique_words)


def remove_stopwords(song_lyrics):
    lines = re.split(r'\n', song_lyrics)
    filtered = ""
    for line in lines:
        line = re.sub(r'[\(\[].*?[\)\]]|\n|\u2005|\u205f', ' ', line)
        filtered += line + 'n'
    lyrics_words = re.split(r',| |_|-|!', filtered)
    stops = stopwords.words('english')
    removed_stopwords = [word for word in lyrics_words if word not in stops and word != '']
    return removed_stopwords


def get_track_data(offset):
    count = offset
    # Dictionary to assign track IDs to the track names, for easy lookup
    tracks = {}

    # get top 50 songs in 2020
    track_results = sp.search(q='year:2018', type='track', limit=50, offset=offset)

    # populate tracks dictionary with track ids as keys, track names as values
    for i, t in enumerate(track_results['tracks']['items']):
        tracks[t['id']] = [t['name'], t['artists'][0]['name']]

    # get audio data for each track in tracks
    audio_data = sp.audio_features(tracks.keys())

    for record in audio_data:
        try:
            print(str(count) + '/10000 songs looked up')
            print(tracks[record['id']][0] + " | " + tracks[record['id']][1])
            record['name'] = tracks[record['id']][0]
            record['artist'] = tracks[record['id']][1]
            url = get_genius_url(record['name'], record['artist'])
            if url != '':
                lyrics = get_genius_lyrics_from_url(url)
                sentiment_data = lyrical_analysis(lyrics)
                record['num_positive'] = sentiment_data['num_positive']
                record['num_negative'] = sentiment_data['num_negative']
                record['num_neutral'] = sentiment_data['num_neutral']
                record['positivity'] = sentiment_data['positivity']
                record['negativity'] = sentiment_data['negativity']
                record['neutrality'] = sentiment_data['neutrality']
                lyrics = remove_stopwords(lyrics)
                record['word_count'] = len(lyrics)
                record['unique_word_count'] = count_unique_words(lyrics)
            else:
                record['word_count'] = 0
            count += 1
        except Exception as e:
            record['word_count'] = 0
    return [track for track in audio_data if track['word_count'] != 0]


# API Tokens
clientID = '688f828e787d49768560dc3b01ad1527'
clientSecret = '1c92d4cff46546558e68bacdcb17a029'

credentialsManager = SpotifyClientCredentials(client_id=clientID, client_secret=clientSecret)
sp = spotipy.Spotify(client_credentials_manager=credentialsManager)

data_to_save = []

for num in range(0, 1998, 50):
    for track_data in get_track_data(num):
        data_to_save.append(track_data)
fields = data_to_save[0].keys()
with open('./data/tracks2018.csv', 'w') as data_file:
    writer = csv.DictWriter(data_file, fieldnames=fields)
    writer.writeheader()
    writer.writerows(data_to_save)

print(data_to_save)
print('Length of data_to_save: ' + str(len(data_to_save)))
