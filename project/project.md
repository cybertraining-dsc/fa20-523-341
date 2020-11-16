# Music Mood Classification

[![Check Report](https://github.com/cybertraining-dsc/fa20-523-341/workflows/Check%20Report/badge.svg)](https://github.com/cybertraining-dsc/fa20-523-341/actions)

- [ ] please follow our template
- [ ] Abstract and Keywords are missing. 
- [ ] Analysis and conclusion sections are missing. Please add them. 

Kunaal Shah, [fa20-523-341](https://github.com/cybertraining-dsc/fa20-523-312/), [Edit](https://github.com/cybertraining-dsc/fa20-523-341/blob/master/project/project.md)

{{% pageinfo %}}

## Abstract
Music analysis on an individual level is incredibly subjective. A particular song can leave polarizing impressions on the emotions of its listener. One person may find a sense of calm in a piece, while another feels energy. In this study we examine the audio and lyrical features of popular songs in order to create an algorithm to recommend songs to a user based on their mood. We take advantage of the audio data provided by Spotify for each song in their massive library, as well as lyrical data from popular music news and lyrics site, Genius. 

{{< table_of_contents >}}

{{% /pageinfo %}}

**Keywords**: music, mood classification, audio, audio content analysis, lyrics, lyrical analysis, big data, spotify, emotion

## 1. Introduction
The overall mood of a musical piece is generally very difficult to decipher due to the highly subjective nature of music. One person might think a song is energetic and happy, while another may think it is quite sad. This can be attributed to varying interpretations of tone and lyrics in song between different listeners. In this project we study both the audio and lyrical patterns of a song through machine learning and natural language processing (NLP) tools in order to create a 'mood sort algorithm'.

## 2. Related Work
Previous studies take three different ways in classifying the mood of a song according to various mood models by analyzing audio, analyzing lyrics, and analyzing lyrics and audio. Most of these studies have been successful in their goals but have uses a limited collection of songs/words for their analysis[^1][^2]. Perhaps obviously, the best results come when combining audio and lyrics.

When researching existing work, we found two applications that approach music recommendations based on mood, one is called 'moooodify', a free web application developed by an independent music enthusiast, Siddharth Ahuja[^4]. Another website, Organize Your Music, aims to organize a Spotify user's music library based on mood, genre, popularity, style, and other categories [^6]. However, both of these applications do not seem to take into account any lyrical analysis of a song.

Lyrics of a song can be used to learn a lot about music from lexical pattern analysis to gender, genre, and mood analyses. For example, in an individual study a researcher found that female artists tend to mention girls, women, and friends a lot, while male artists sing about late Saturday Nights, play and love [^3]. Another popular project, SongSim, used repetition to visualize the parts of a song [^5]. Findings such as these can be used to uncover the gender of an artist based on their lyrics. Similarly, by use of NLP tools, lyrical text can be analyzed to elicit the mood and emotion of a song.

A simple weighting is given by a study from the University of Illinois to categorize moods of a song by audio and lyrical content analysis.

```phybrid = \alpha plyrics + (1 - \alpha )paudio```

where a is the probability weight given by the lyrical classifier[^1].


## 3. Datasets
For the audio content analysis portion of this project, we use Spotify's Web API, which provides a great amount audio data for every song in Spotify's song collection, including valence, energy, and danceability.

For the lyrical analysis portion of this project, we use Genius's API to pull lyrics information for a song. Genius is a website which contains lyrics to several popular songs. We will then use WordNet, which is large collection of English lexicon, used to classify words and phrases with features such as valence, arousal, dominance.


## Project Goals 
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
 
## Analysis

## Conclusion

## References
[^1]: [Improving Mood Classification in Music Digital Libraries by Combining Lyrics and Audio](https://dl.acm.org/doi/10.1145/1816123.1816146)

[^2]: [Lyric Text Mining in Mood Classification](https://www.researchgate.net/publication/220723046_Lyric_Text_Mining_in_Music_Mood_Classification)

[^3]: [What Songs Tell Us About: Text Mining with Lyrics](https://towardsdatascience.com/what-songs-tell-us-about-text-mining-with-lyrics-ca80f98b3829)

[^4]: [Sort your music by any mood — Introducing moooodify](https://blog.usejournal.com/sort-your-music-by-any-mood-introducing-moooodify-41749e80faab)

[^5]: [SongSim](https://colinmorris.github.io/SongSim/#/)

[^6]: [Organize Your Music](http://organizeyourmusic.playlistmachinery.com/)
