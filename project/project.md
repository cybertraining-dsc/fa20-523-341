# Music Mood Classification

Kunaal Shah, [fa20-523-341](https://github.com/cybertraining-dsc/fa20-523-312/), [Edit](https://github.com/cybertraining-dsc/fa20-523-341/blob/master/project/project.md)

{{% pageinfo %}}

{{< table_of_contents >}}

{{% pageinfo %}}
## Introduction
The overall mood of a musical piece is generally very difficult to decipher due to the highly subjective nature of music. One person might think a song is energetic and happy, while another may think it is quite sad. This can be attributed to varying interpretations of tone and lyrics in song between different listeners. In this project we study both the audio and lyrical patterns of a song through machine learning and natural language processing (NLP) tools in order to create a 'mood sort algorithm'.

## Related Work
Previous studies take three different ways in classifying the mood of a song according to various mood models by analyzing audio, analyzing lyrics, and analyzing lyrics and audio. Most of these studies have been successful in their goals but have uses a limited collection of songs/words for their analysis[^1][^2]. Perhaps obviously, the best results come when combining audio and lyrics.

When researching existing work, we found two applications that approach music recommendations based on mood, one is called 'moooodify', a free web application developed by an independent music enthusiast, Siddharth Ahuja[^4]. Another website, Organize Your Music, aims to organize a Spotify user's music library based on mood, genre, popularity, style, and other categories [^6]. However, both of these applications do not seem to take into account any lyrical analysis of a song.

Lyrics of a song can be used to learn a lot about music from lexical pattern analysis to gender, genre, and mood analyses. For example, in an individual study a researcher found that female artists tend to mention girls, women, and friends a lot, while male artists sing about late Saturday Nights, play and love [^3]. Another popular project, SongSim, used repetition to visualize the parts of a song [^5]. Findings such as these can be used to uncover the gender of an artist based on their lyrics. Similarly, by use of NLP tools, lyrical text can be analyzed to elicit the mood and emotion of a song.

A simple weighting is given by a study from the University of Illinois to categorize moods of a song by audio and lyrical content analysis.
```phybrid = \alpha plyrics + (1 - \alpha )paudio```
Where a is the probability weight given by the lyrical classifier[^1].


## Datasets
For the audio content analysis portion of this project, we use Spotify's Web API, which provides a great amount audio data for every song in Spotify's song collection, including valence, energy, and danceability.

For the lyrical analysis portion of this project, we use Genius's API to pull lyrics information for a song. Genius is a website which contains lyrics to several popular songs. We will then use WordNet, which is large collection of English lexicon, used to classify words and phrases with features such as valence, arousal, dominance.


## Project Goals


## References
[^1]: [Improving Mood Classification in Music Digital Libraries by Combining Lyrics and Audio](https://dl.acm.org/doi/10.1145/1816123.1816146)

[^2]: [Lyric Text Mining in Mood Classification](https://www.researchgate.net/publication/220723046_Lyric_Text_Mining_in_Music_Mood_Classification)

[^3]: [What Songs Tell Us About: Text Mining with Lyrics](https://towardsdatascience.com/what-songs-tell-us-about-text-mining-with-lyrics-ca80f98b3829)

[^4]: [Sort your music by any mood — Introducing moooodify](https://blog.usejournal.com/sort-your-music-by-any-mood-introducing-moooodify-41749e80faab)

[^5]: [SongSim](https://colinmorris.github.io/SongSim/#/)

[^6]: [Organize Your Music](http://organizeyourmusic.playlistmachinery.com/)
