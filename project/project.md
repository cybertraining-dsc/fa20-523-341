# Music Mood Classification

[![Check Report](https://github.com/cybertraining-dsc/fa20-523-341/workflows/Check%20Report/badge.svg)](https://github.com/cybertraining-dsc/fa20-523-341/actions)
[![Status](https://github.com/cybertraining-dsc/fa20-523-341/workflows/Status/badge.svg)](https://github.com/cybertraining-dsc/fa20-523-341/actions)
Status: in progress

Kunaal Shah, [fa20-523-341](https://github.com/cybertraining-dsc/fa20-523-312/), [Edit](https://github.com/cybertraining-dsc/fa20-523-341/blob/master/project/project.md)

{{% pageinfo %}}

## Abstract

Music analysis on an individual level is incredibly subjective. A particular song can leave polarizing impressions on the emotions of its listener. One person may find a sense of calm in a piece, while another feels energy. In this study we examine the audio and lyrical features of popular songs in order to create an algorithm to recommend songs to a user based on their mood. We take advantage of the audio data provided by Spotify for each song in their massive library, as well as lyrical data from popular music news and lyrics site, Genius. 

Contents

{{< table_of_contents >}}

{{% /pageinfo %}}

**Keywords:** music, mood classification, audio, audio content analysis, lyrics, lyrical analysis, big data, spotify, emotion

## 1. Introduction

The overall mood of a musical piece is generally very difficult to decipher due to the highly subjective nature of music. One person might think a song is energetic and happy, while another may think it is quite sad. This can be attributed to varying interpretations of tone and lyrics in song between different listeners. In this project we study both the audio and lyrical patterns of a song through machine learning and natural language processing (NLP) tools in order to create a 'mood sort algorithm'.

## 2. Related Work

Previous studies take three different ways in classifying the mood of a song according to various mood models by analyzing audio, analyzing lyrics, and analyzing lyrics and audio. Most of these studies have been successful in their goals but have uses a limited collection of songs/words for their analysis [^1][^2]. Perhaps obviously, the best results come when combining audio and lyrics.

When researching existing work, we found two applications that approach music recommendations based on mood, one is called 'moooodify', a free web application developed by an independent music enthusiast, Siddharth Ahuja [^4]. Another website, Organize Your Music, aims to organize a Spotify user's music library based on mood, genre, popularity, style, and other categories [^6]. However, both of these applications do not seem to take into account any lyrical analysis of a song.

Lyrics of a song can be used to learn a lot about music from lexical pattern analysis to gender, genre, and mood analyses. For example, in an individual study a researcher found that female artists tend to mention girls, women, and friends a lot, while male artists sing about late Saturday Nights, play and love [^3]. Another popular project, SongSim, used repetition to visualize the parts of a song [^5]. Findings such as these can be used to uncover the gender of an artist based on their lyrics. Similarly, by use of NLP tools, lyrical text can be analyzed to elicit the mood and emotion of a song.

A simple weighting is given by a study from the University of Illinois to categorize moods of a song by audio and lyrical content analysis.

```phybrid = \alpha plyrics + (1 - \alpha )paudio```

where a is the probability weight given by the lyrical classifier [^1].


## 3. Datasets

For the audio content analysis portion of this project, we use Spotify's Web API, which provides a great amount audio data for every song in Spotify's song collection, including valence, energy, and danceability.

For the lyrical analysis portion of this project, we use Genius's API to pull lyrics information for a song. Genius is a website which contains lyrics to several popular songs. We will then use WordNet, which is large collection of English lexicon, used to classify words and phrases with features such as valence, arousal, dominance.


## 4. Project Goals 

 - make dataset of collected song information from spotify and genius api 
 - Analyze audio and lyrical data of top songs on spotify
   - graphs and statistics of data fields like valence, danceability, word count, etc
   - note current trends in song types
 - determine a song's overall positivity - postive / negative lyrics
   - potential simple rating system : (positive_words - negative_words / total_words ) 
   - **Note: words can be neutral**
 - Make sense of emotions portrayed by the songs based off of audio/lyrical data
 - generate ability to generate list of songs relevant to input mood
   - user enters mood on scale from 0-1, receives a list of songs
 
## 5. Analysis

### 5.1 Data Collection

#### 5.1.1 Accumulating lyrics

From our data sources, we collected data for roughly 10000 of the most popular songs released between 2017 and 2020, taking account of several audio and lyrical features present in the track. We gathered this data by hand, first querying the most popular 2000 newly released songs in each year between 2017 and 2020. We then sent requests to Genius to gather lyrics for each song. Some songs, even though they were popular did not have lyrics present on Genius, these songs were excluded from our dataset. With BeautifulSOup, we extracted and cleaned up the lyrics, removing anything that is not a part of the song's lyrics like annotations left by users, section headings (Chorus, Hook, etc), and empty lines. After exclusions our data covered a little over 6000 Spotify tracks 

#### Performance of sentiment analysis on lyrics

With a song's lyrics in hand, we used NLTK's sentiment module, Vader, to read each line in the lyrics. NLTK Vader reads a line of text and gives a scores on positivity, negativity, neutrality, and and overall compound score. We marked lines with a compound score greater than 0.5 as positive, less than -0.1 as negative, and anything in between as neutral. We then found the percentages of positive, negative, and neutral lines in a song's composition and saved them to our data set. 

We performed a brief analysis of the legibility of the Vader module in determining sentiment on four separate strings. "I'm happy" and "I'm so happy" were used to compare two positive lines, "I'm happy" was expected to have a positive compound score, but slightly less positive than "I'm so happy". Similarly, we used two negative lines "I'm sad" and the slightly more extreme, "I'm so sad" which were expected to result in negative compound scores with "I'm sad" being less negative than "I'm so sad".

```
Scores for 'I'm happy': {
   'neg': 0.0, 
   'neu': 0.213, 
   'pos': 0.787, 
   'compound': 0.5719
}

Scores for 'I'm so happy': {'neg': 0.0, 'neu': 0.334, 'pos': 0.666, 'compound': 0.6115}

Scores for 'I'm sad': {'neg': 0.756, 'neu': 0.244, 'pos': 0.0, 'compound': -0.4767}

Scores for 'I'm so sad': {'neg': 0.629, 'neu': 0.371, 'pos': 0.0, 'compound': -0.5256}
```

While these results confirmed our expectations, one issue that comes to the table is that Vader takes into consideration additional string features such as punctuation in its determination of score, meaning "I'm so sad!" will be more negative than "I'm so sad". Since lyrics on Genius are contributed by the community, in most cases there is a lack of consistency using accurate punctuation. Additionally in some cases there can be typos present in a line of lyrics, both of which can skew our data. However we determined that our method in using the Vader module is suitable for our project as we simply want to determine if a track is positive or negative without needing to be too specific.

In addition to performing sentiment analysis on the lyrics, we tokenized the lyrics, removing common words such as 'a', 'the','for', etc. This was done to collect data on the number of meaningful and number of non-repeating words in each song. Albeit while this data was never used in our study, it could prove useful in future studies.

*Table 1* displays a snapshot of the data we collected from seven tracks released in 2020. The dataset contains 27 fields, 13 of which describe the audio content of a track, and 8 of which describe the lyrics of the track.


| danceability | energy | key | loudness | mode | speechiness | acousticness | instrumentalness | liveness | valence | tempo   | type           | id                     | uri                                  | track_href                                               | analysis_url                                                     | duration_ms | time_signature | name                    | artist         | num_positive | num_negative | num_neutral | positivity  | negativity  | neutrality  | word_count | unique_word_count |
|--------------|--------|-----|----------|------|-------------|--------------|------------------|----------|---------|---------|----------------|------------------------|--------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|-------------|----------------|-------------------------|----------------|--------------|--------------|-------------|-------------|-------------|-------------|------------|-------------------|
| 0.709        | 0.548  | 10  | -8.493   | 1    | 0.353       | 0.65         | 1.59E-06         | 0.133    | 0.543   | 83.995  | audio_features | 1tkg4EHVoqnhR6iFEXb60y | spotify:track:1tkg4EHVoqnhR6iFEXb60y | https://api.spotify.com/v1/tracks/1tkg4EHVoqnhR6iFEXb60y | https://api.spotify.com/v1/audio-analysis/1tkg4EHVoqnhR6iFEXb60y | 160000      | 4              | What You Know Bout Love | Pop Smoke      | 7            | 2            | 33          | 0.166666667 | 0.047619048 | 0.785714286 | 209        | 130               |
| 0.799        | 0.66   | 1   | -6.153   | 0    | 0.079       | 0.256        | 0                | 0.111    | 0.471   | 140.04  | audio_features | 02kDW379Yfd5PzW5A6vuGt | spotify:track:02kDW379Yfd5PzW5A6vuGt | https://api.spotify.com/v1/tracks/02kDW379Yfd5PzW5A6vuGt | https://api.spotify.com/v1/audio-analysis/02kDW379Yfd5PzW5A6vuGt | 195429      | 4              | Lemonade                | Internet Money | 8            | 15           | 34          | 0.140350877 | 0.263157895 | 0.596491228 | 307        | 177               |
| 0.514        | 0.73   | 1   | -5.934   | 1    | 0.0598      | 0.00146      | 9.54E-05         | 0.0897   | 0.334   | 171.005 | audio_features | 0VjIjW4GlUZAMYd2vXMi3b | spotify:track:0VjIjW4GlUZAMYd2vXMi3b | https://api.spotify.com/v1/tracks/0VjIjW4GlUZAMYd2vXMi3b | https://api.spotify.com/v1/audio-analysis/0VjIjW4GlUZAMYd2vXMi3b | 200040      | 4              | Blinding Lights         | The Weeknd     | 3            | 10           | 22          | 0.085714286 | 0.285714286 | 0.628571429 | 150        | 75                |
| 0.65         | 0.613  | 9   | -6.13    | 0    | 0.128       | 0.00336      | 0                | 0.267    | 0.0804  | 149.972 | audio_features | 2U5WueTLIK5WJLD7mvDODv | spotify:track:2U5WueTLIK5WJLD7mvDODv | https://api.spotify.com/v1/tracks/2U5WueTLIK5WJLD7mvDODv | https://api.spotify.com/v1/audio-analysis/2U5WueTLIK5WJLD7mvDODv | 194621      | 4              | Wishing Well            | Juice WRLD     | 0            | 22           | 30          | 0           | 0.423076923 | 0.576923077 | 238        | 104               |
| 0.737        | 0.802  | 0   | -4.771   | 1    | 0.0878      | 0.468        | 0                | 0.0931   | 0.682   | 144.015 | audio_features | 35mvY5S1H3J2QZyna3TFe0 | spotify:track:35mvY5S1H3J2QZyna3TFe0 | https://api.spotify.com/v1/tracks/35mvY5S1H3J2QZyna3TFe0 | https://api.spotify.com/v1/audio-analysis/35mvY5S1H3J2QZyna3TFe0 | 172325      | 4              | positions               | Ariana Grande  | 10           | 5            | 33          | 0.208333333 | 0.104166667 | 0.6875      | 178        | 73                |
| 0.357        | 0.425  | 5   | -7.301   | 1    | 0.0333      | 0.584        | 0                | 0.322    | 0.27    | 102.078 | audio_features | 4xqrdfXkTW4T0RauPLv3WA | spotify:track:4xqrdfXkTW4T0RauPLv3WA | https://api.spotify.com/v1/tracks/4xqrdfXkTW4T0RauPLv3WA | https://api.spotify.com/v1/audio-analysis/4xqrdfXkTW4T0RauPLv3WA | 198040      | 3              | Heather                 | Conan Gray     | 3            | 4            | 22          | 0.103448276 | 0.137931034 | 0.75862069  | 114        | 66                |
| 0.83         | 0.585  | 0   | -6.476   | 1    | 0.094       | 0.237        | 0                | 0.248    | 0.485   | 109.978 | audio_features | 6Im9k8u9iIzKMrmV7BWtlF | spotify:track:6Im9k8u9iIzKMrmV7BWtlF | https://api.spotify.com/v1/tracks/6Im9k8u9iIzKMrmV7BWtlF | https://api.spotify.com/v1/audio-analysis/6Im9k8u9iIzKMrmV7BWtlF | 173711      | 4              | 34+35                   | Ariana Grande  | 3            | 13           | 52          | 0.044117647 | 0.191176471 | 0.764705882 | 249        | 127               |

**Table 1:** Snapshot of dataset containing tracks released in 2020

#### Description of select data fields

The following terms defined are important in our analyses. In our data set most terms contain are represented by a  value between 0 and 1, indicating least to most. For example, looking at the first two rows in *Table 1*, we can see that the track by the artist, Pop Smoke, has a greater speechiness score, indicating a greater percentage of that song contains spoken word. 
 
- **Danceability:** uses several musical elements (tempo, stability, beat strength, regularity) to determine how suitable a given track is for dancing
- **Energy:**  measures intensity of a song
- **Loudness:** average loudness (in decibels) of a track
- **Mode:** indicates whether track uses major(0) or minor (1) scale
- **Speechiness:** identifies how much of a track contains spoken word
- **Instrumentalness:** confidence value on a track having no vocal content
- **Valence:** predicts the overall happiness, or positivity of a track based on its musical features
- **Tempo:** average tempo of a track
- **Positivity** percentage of lines in a song's lyrics determined to have a positive sentiment score
- **Negativity** percentage of lines in a song's lyrics determined to have a negative sentiment score

Out of these fields, we seek to find which audio features correlate to a song's valence and if our positivity and negativity scores of a song's lyrics provide any meaningfullness in determining a song's positivity. For the purpose of this study we mainly focus on valence, energy, danceability, positivity, and negativity.

#### Preliminary Analysis of Data

![Heatmap](https://github.com/cybertraining-dsc/fa20-523-341/raw/main/project/images/all_tracks_heatmap.png)

**Figure 1:** Heatmap of data with fields valence, energy, danceability, positivity, negativity

Referring to *Figure 1*, we find that track lyrics tend to be more negative than positive. However for the most part, even with tracks with negative lyrics, the valence, or overall happiness of the audio features hovers around 0.5; indicating that most songs tend to have neutral audio features. Looking at tracks with lyrics that are highly positive we find that the valence rises to about 0.7 to 0.8 and that songs with extremely high negatively also cause the valence to drop to the 0.3 range. These observations indicate that only extremes in lyrical sentiment correlate significantly in a song's valence, as some songs with negative lyrics may also be fast-tempo and energetic, keeping the valence relatively high compared to lyrical composition. This is shown in our visualization, where both tracks with positive and negative lyricals have high energy and danceability values, indicating fast-tempos and high-pitches.

## 6. Conclusion

There are several aspects that could be improved upon in future iterations of our study. In this project we only worked with songs released after 2017, but obviously, people would still enjoy listening to songs from previous years. The Spotiy API contains audio features data for every song in its library, so it would be worth collecting that data on every song for usage in the generation of song recommendations. Secondly, our data set excluded songs on Spotify, whose lyrics could not be found easily on Genius.com. We should have handled these cases by attempting to find the lyrics from other popular websites which store music lyrics. And lastly, we worked with a very small dataset relative to the total amount of songs that exist, or that are available on Spotify. There is great possibility in repeating this study quite easily with a greater selection of songs. We were suprised by how small the file sizes were of our dataset of 6000 songs, the aggregated data set being only 2.3 megabytes in size. Using that value a set of one million songs can be estimated to only be around 350 megabytes. 

This section will be expanded upon after completion of analyses

## 7. References

[^1]: Hu, X., &amp; Downie, J. S. (2010). Improving mood classification in music digital libraries by combining lyrics and audio. Proceedings of the 10th Annual Joint Conference on Digital Libraries - JCDL '10. doi:10.1145/1816123.1816146

[^2]: Kashyap, N., Choudhury, T., Chaudhary, D. K., &amp; Lal, R. (2016). Mood Based Classification of Music by Analyzing Lyrical Data Using Text Mining. 2016 International Conference on Micro-Electronics and Telecommunication Engineering (ICMETE). doi:10.1109/icmete.2016.65

[^3]: Jeong, J. (2019, January 19). What Songs Tell Us About: Text Mining with Lyrics. Retrieved November 17, 2020, from https://towardsdatascience.com/what-songs-tell-us-about-text-mining-with-lyrics-ca80f98b3829

[^4]: Ahuja, S. (2019, September 25). Sort your music by any mood - Introducing moooodify. Retrieved November 17, 2020, from https://blog.usejournal.com/sort-your-music-by-any-mood-introducing-moooodify-41749e80faab

[^5]: Morris, C. (2016). SongSim. Retrieved November 17, 2020, from https://colinmorris.github.io/SongSim/

[^6]: Lamere, P. (2016, August 6). Organize Your Music. Retrieved November 17, 2020, from http://organizeyourmusic.playlistmachinery.com/

[^7]: Get Audio Features for a Track. (2020). Retrieved November 17, 2020, from https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/
