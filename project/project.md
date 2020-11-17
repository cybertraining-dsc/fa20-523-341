# Music Mood Classification

[![Check Report](https://github.com/cybertraining-dsc/fa20-523-341/workflows/Check%20Report/badge.svg)](https://github.com/cybertraining-dsc/fa20-523-341/actions)

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

From our data sources, we collected data for roughly 8000 songs released between 2017 and 2020, taking account of several audio and lyrical features present in the track. Below is a a sample view of the data from seven tracks released in 2020. 

### Data Sample

| danceability | energy | key | loudness | mode | speechiness | acousticness | instrumentalness | liveness | valence | tempo   | type           | id                     | uri                                  | track_href                                               | analysis_url                                                     | duration_ms | time_signature | name                    | artist         | num_positive | num_negative | num_neutral | positivity  | negativity  | neutrality  | word_count | unique_word_count |
|--------------|--------|-----|----------|------|-------------|--------------|------------------|----------|---------|---------|----------------|------------------------|--------------------------------------|----------------------------------------------------------|------------------------------------------------------------------|-------------|----------------|-------------------------|----------------|--------------|--------------|-------------|-------------|-------------|-------------|------------|-------------------|
|              |        |     |          |      |             |              |                  |          |         |         |                |                        |                                      |                                                          |                                                                  |             |                |                         |                |              |              |             |             |             |             |            |                   |
| 0.709        | 0.548  | 10  | -8.493   | 1    | 0.353       | 0.65         | 1.59E-06         | 0.133    | 0.543   | 83.995  | audio_features | 1tkg4EHVoqnhR6iFEXb60y | spotify:track:1tkg4EHVoqnhR6iFEXb60y | https://api.spotify.com/v1/tracks/1tkg4EHVoqnhR6iFEXb60y | https://api.spotify.com/v1/audio-analysis/1tkg4EHVoqnhR6iFEXb60y | 160000      | 4              | What You Know Bout Love | Pop Smoke      | 7            | 2            | 33          | 0.166666667 | 0.047619048 | 0.785714286 | 209        | 130               |
|              |        |     |          |      |             |              |                  |          |         |         |                |                        |                                      |                                                          |                                                                  |             |                |                         |                |              |              |             |             |             |             |            |                   |
| 0.799        | 0.66   | 1   | -6.153   | 0    | 0.079       | 0.256        | 0                | 0.111    | 0.471   | 140.04  | audio_features | 02kDW379Yfd5PzW5A6vuGt | spotify:track:02kDW379Yfd5PzW5A6vuGt | https://api.spotify.com/v1/tracks/02kDW379Yfd5PzW5A6vuGt | https://api.spotify.com/v1/audio-analysis/02kDW379Yfd5PzW5A6vuGt | 195429      | 4              | Lemonade                | Internet Money | 8            | 15           | 34          | 0.140350877 | 0.263157895 | 0.596491228 | 307        | 177               |
|              |        |     |          |      |             |              |                  |          |         |         |                |                        |                                      |                                                          |                                                                  |             |                |                         |                |              |              |             |             |             |             |            |                   |
| 0.514        | 0.73   | 1   | -5.934   | 1    | 0.0598      | 0.00146      | 9.54E-05         | 0.0897   | 0.334   | 171.005 | audio_features | 0VjIjW4GlUZAMYd2vXMi3b | spotify:track:0VjIjW4GlUZAMYd2vXMi3b | https://api.spotify.com/v1/tracks/0VjIjW4GlUZAMYd2vXMi3b | https://api.spotify.com/v1/audio-analysis/0VjIjW4GlUZAMYd2vXMi3b | 200040      | 4              | Blinding Lights         | The Weeknd     | 3            | 10           | 22          | 0.085714286 | 0.285714286 | 0.628571429 | 150        | 75                |
|              |        |     |          |      |             |              |                  |          |         |         |                |                        |                                      |                                                          |                                                                  |             |                |                         |                |              |              |             |             |             |             |            |                   |
| 0.65         | 0.613  | 9   | -6.13    | 0    | 0.128       | 0.00336      | 0                | 0.267    | 0.0804  | 149.972 | audio_features | 2U5WueTLIK5WJLD7mvDODv | spotify:track:2U5WueTLIK5WJLD7mvDODv | https://api.spotify.com/v1/tracks/2U5WueTLIK5WJLD7mvDODv | https://api.spotify.com/v1/audio-analysis/2U5WueTLIK5WJLD7mvDODv | 194621      | 4              | Wishing Well            | Juice WRLD     | 0            | 22           | 30          | 0           | 0.423076923 | 0.576923077 | 238        | 104               |
|              |        |     |          |      |             |              |                  |          |         |         |                |                        |                                      |                                                          |                                                                  |             |                |                         |                |              |              |             |             |             |             |            |                   |
| 0.737        | 0.802  | 0   | -4.771   | 1    | 0.0878      | 0.468        | 0                | 0.0931   | 0.682   | 144.015 | audio_features | 35mvY5S1H3J2QZyna3TFe0 | spotify:track:35mvY5S1H3J2QZyna3TFe0 | https://api.spotify.com/v1/tracks/35mvY5S1H3J2QZyna3TFe0 | https://api.spotify.com/v1/audio-analysis/35mvY5S1H3J2QZyna3TFe0 | 172325      | 4              | positions               | Ariana Grande  | 10           | 5            | 33          | 0.208333333 | 0.104166667 | 0.6875      | 178        | 73                |
|              |        |     |          |      |             |              |                  |          |         |         |                |                        |                                      |                                                          |                                                                  |             |                |                         |                |              |              |             |             |             |             |            |                   |
| 0.357        | 0.425  | 5   | -7.301   | 1    | 0.0333      | 0.584        | 0                | 0.322    | 0.27    | 102.078 | audio_features | 4xqrdfXkTW4T0RauPLv3WA | spotify:track:4xqrdfXkTW4T0RauPLv3WA | https://api.spotify.com/v1/tracks/4xqrdfXkTW4T0RauPLv3WA | https://api.spotify.com/v1/audio-analysis/4xqrdfXkTW4T0RauPLv3WA | 198040      | 3              | Heather                 | Conan Gray     | 3            | 4            | 22          | 0.103448276 | 0.137931034 | 0.75862069  | 114        | 66                |
|              |        |     |          |      |             |              |                  |          |         |         |                |                        |                                      |                                                          |                                                                  |             |                |                         |                |              |              |             |             |             |             |            |                   |
| 0.83         | 0.585  | 0   | -6.476   | 1    | 0.094       | 0.237        | 0                | 0.248    | 0.485   | 109.978 | audio_features | 6Im9k8u9iIzKMrmV7BWtlF | spotify:track:6Im9k8u9iIzKMrmV7BWtlF | https://api.spotify.com/v1/tracks/6Im9k8u9iIzKMrmV7BWtlF | https://api.spotify.com/v1/audio-analysis/6Im9k8u9iIzKMrmV7BWtlF | 173711      | 4              | 34+35                   | Ariana Grande  | 3            | 13           | 52          | 0.044117647 | 0.191176471 | 0.764705882 | 249        | 127               |

**Figure 1:** Snapshot of dataset containing tracks released in 2020

### Key Terms
The following terms defined are important in our analyses. In our data set most terms contain are represented by a  value between 0 and 1, indicating least to most. For example, looking at the first two rows in Figure 1, we can see that the track by the artist, Pop Smoke, has a greater speechiness score, indicating a greater percentage of that song contains spoken word. 
 
- Danceability: uses several musical elements (tempo, stability, beat strength, regularity) to determine how suitable a given track is for dancing
- Energy: 
- Loudness: 
- Mode: 
- Speechiness: 
- Acousticness:
- instrumentalness:
- liveness:
- valence:
- tempo:

## 6. Conclusion

There are several aspects that could be improved upon in future iterations of our study. In this project we only worked with songs released after 2017, but obviously, people would still enjoy listening to songs from previous years. The Spotiy API contains audio features data for every song in its library, so it would be worth collecting that data on every song for usage in the generation of song recommendations. Secondly, our data set excluded songs on Spotify, whose lyrics could not be found easily on Genius.com. We should have handled these cases by attempting to find the lyrics from other popular websites which store music lyrics. And lastly, we worked with a very small dataset relative to the total amount of songs that exist, or that are available by Spotify.

This section will be expanded upon after completion of analyses

## 7. References

[^1]: Hu, X., &amp; Downie, J. S. (2010). Improving mood classification in music digital libraries by combining lyrics and audio. Proceedings of the 10th Annual Joint Conference on Digital Libraries - JCDL '10. doi:10.1145/1816123.1816146

[^2]: Kashyap, N., Choudhury, T., Chaudhary, D. K., &amp; Lal, R. (2016). Mood Based Classification of Music by Analyzing Lyrical Data Using Text Mining. 2016 International Conference on Micro-Electronics and Telecommunication Engineering (ICMETE). doi:10.1109/icmete.2016.65

[^3]: Jeong, J. (2019, January 19). What Songs Tell Us About: Text Mining with Lyrics. Retrieved November 17, 2020, from https://towardsdatascience.com/what-songs-tell-us-about-text-mining-with-lyrics-ca80f98b3829

[^4]: Ahuja, S. (2019, September 25). Sort your music by any mood - Introducing moooodify. Retrieved November 17, 2020, from https://blog.usejournal.com/sort-your-music-by-any-mood-introducing-moooodify-41749e80faab

[^5]: Morris, C. (2016). SongSim. Retrieved November 17, 2020, from https://colinmorris.github.io/SongSim/

[^6]: Lamere, P. (2016, August 6). Organize Your Music. Retrieved November 17, 2020, from http://organizeyourmusic.playlistmachinery.com/

[^7]: Get Audio Features for a Track. (2020). Retrieved November 17, 2020, from https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/
