# Music Mood Classification

[![Check Report](https://github.com/cybertraining-dsc/fa20-523-341/workflows/Check%20Report/badge.svg)](https://github.com/cybertraining-dsc/fa20-523-341/actions)
[![Status](https://github.com/cybertraining-dsc/fa20-523-341/workflows/Status/badge.svg)](https://github.com/cybertraining-dsc/fa20-523-341/actions)
Status: final, Type: Project

Kunaal Shah, [fa20-523-341](https://github.com/cybertraining-dsc/fa20-523-312/), [Edit](https://github.com/cybertraining-dsc/fa20-523-341/blob/master/project/project.md)

{{% pageinfo %}}

## Abstract

Music analysis on an individual level is incredibly subjective. A particular song can leave polarizing impressions on the emotions of its listener. One person may find a sense of calm in a piece, while another feels energy. In this study we examine the audio and lyrical features of popular songs in order to find relationships in a song's lyrics, audio features, and its valence. We take advantage of the audio data provided by Spotify for each song in their massive library, as well as lyrical data from popular music news and lyrics site, Genius. 

Contents

{{< table_of_contents >}}

{{% /pageinfo %}}

**Keywords:** music, mood classification, audio, audio content analysis, lyrics, lyrical analysis, big data, spotify, emotion

## 1. Introduction

The overall mood of a musical piece is generally very difficult to decipher due to the highly subjective nature of music. One person might think a song is energetic and happy, while another may think it is quite sad. This can be attributed to varying interpretations of tone and lyrics in song between different listeners. In this project we study both the audio and lyrical patterns of a song through machine learning and natural language processing (NLP) to find a relationship between the song's lyrics and its valence, or its overall positivity.

## 2. Related Work

Previous studies take three different ways in classifying the mood of a song according to various mood models by analyzing audio, analyzing lyrics, and analyzing lyrics and audio. Most of these studies have been successful in their goals but have uses a limited collection of songs/words for their analysis [^2]. Perhaps obviously, the best results come when combining audio and lyrics. A simple weighting is given by a study from the University of Illinois to categorize moods of a song by audio and lyrical content analysis, A simple weighting is given by a study from the University of Illinois to categorize moods of a song by audio and lyrical content analysis.

```phybrid = \alpha plyrics + (1 - \alpha )paudio```

When researching existing work, we found two applications that approach music recommendations based on mood, one is called 'moooodify', a free web application developed by an independent music enthusiast, Siddharth Ahuja [^4]. Another website, Organize Your Music, aims to organize a Spotify user's music library based on mood, genre, popularity, style, and other categories [^6]. However, both of these applications do not seem to take into account any lyrical analysis of a song.

Lyrics of a song can be used to learn a lot about music from lexical pattern analysis to gender, genre, and mood analyses. For example, in an individual study a researcher found that female artists tend to mention girls, women, and friends a lot, while male artists sing about late Saturday Nights, play and love [^3]. Another popular project, SongSim, used repetition to visualize the parts of a song [^5]. Findings such as these can be used to uncover the gender of an artist based on their lyrics. Similarly, by use of NLP tools, lyrical text can be analyzed to elicit the mood and emotion of a song.

## 3. Datasets

For the audio content analysis portion of this project, we use Spotify's Web API, which provides a great amount audio data for every song in Spotify's song collection, including valence, energy, and danceability [^7].

For the lyrical analysis portion of this project, we use Genius's API to pull lyrics information for a song. Genius is a website where users submit lyrics and annotations to several popular songs [^8]. To perform sentiment analysis on a set of lyrics collected from Genius, we use the NLTK Vader library.

## 4. Analysis

For the purposes of this study, we analyze a track's lyrics and assign them scores based on their positivity, negativity, and neutrality. We then append this data to the audio feature data we receive from Spotify. To compare and find relationships and meaningfulness in using lyrics and audio features to predict a song's valence, we employ several statistical and machine learning approaches. We try linear regression and polynomial regression to find relationships between several features of a track and a song's valence. Then we perform multivariate linear regression to find how accurately we can predict a song's valence based on the audio and lyrical features available in our dataset. 

### 4.1 Accumulation of audio features and lyrics

From our data sources, we collected data for roughly 10000 of the most popular songs released between 2017 and 2020, taking account of several audio and lyrical features present in the track. We gathered this data by hand, first querying the most popular 2000 newly released songs in each year between 2017 and 2020. We then sent requests to Genius to gather lyrics for each song. Some songs, even though they were popular, did not have lyrics present on Genius, these songs were excluded from our dataset. With BeautifulSoup, we extracted and cleaned up the lyrics, removing anything that is not a part of the song's lyrics like annotations left by users, section headings (Chorus, Hook, etc), and empty lines. After exclusions our data covered 6551 Spotify tracks.

### 4.2 Performance of sentiment analysis on lyrics

With a song's lyrics in hand, we used NLTK's sentiment module, Vader, to read each line in the lyrics. NLTK Vader Sentiment Intensity Analyzer is a pretrained machine learning model that reads a line of text and assigns it scores of positivity, negativity, neutrality, and and overall compound score. We marked lines with a compound score greater than 0.5 as positive, less than -0.1 as negative, and anything in between as neutral. We then found the percentages of positive, negative, and neutral lines in a song's composition and saved them to our dataset. 

We performed a brief analysis of the legibility of the Vader module in determining sentiment on four separate strings. "I'm happy" and "I'm so happy" were used to compare two positive lines, "I'm happy" was expected to have a positive compound score, but slightly less positive than "I'm so happy". Similarly, we used two negative lines "I'm sad" and the slightly more extreme, "I'm so sad" which were expected to result in negative compound scores with "I'm sad" being less negative than "I'm so sad".

```
Scores for 'I'm happy': {
    'neg': 0.0, 
    'neu': 0.213, 
    'pos': 0.787, 
    'compound': 0.5719
}

Scores for 'I'm so happy': {
    'neg': 0.0, 
    'neu': 0.334, 
    'pos': 0.666, 
    'compound': 0.6115
}

Scores for 'I'm sad': {
    'neg': 0.756, 
    'neu': 0.244, 
    'pos': 0.0, 
    'compound': -0.4767
}

Scores for 'I'm so sad': {
    'neg': 0.629, 
    'neu': 0.371, 
    'pos': 0.0, 
    'compound': -0.5256
}
```

While these results confirmed our expectations, a few issues come to the table with our use of the Vader module. One is that Vader takes into consideration additional string features such as punctuation in its determination of score, meaning "I'm so sad!" will be more negative than "I'm so sad". Since lyrics on Genius are contributed by the community, in most cases there is a lack of consistency using accurate punctuation. Additionally, in some cases there can be typos present in a line of lyrics, both of which can skew our data. However we determined that our method in using the Vader module is suitable for our project as we simply want to determine if a track is positive or negative without needing to be too specific. Another issue is that our implementation of Vader acts only on English words. Again, since lyrics on Genius are contributed by the community, there could be errors in our data from misspelled word contributions as well as sections or entire lyrics written in different languages.

In addition to performing sentiment analysis on the lyrics, we tokenized the lyrics, removing common words such as 'a', 'the','for', etc. This was done to collect data on the number of meaningful and number of non-repeating words in each song. Albeit while this data was never used in our study, it could prove useful in future studies.

*Table 1* displays a snapshot of the data we collected from seven tracks released in 2020. The dataset contains 27 fields, 12 of which describe the audio features of a track, and 8 of which describe the lyrics of the track. For the purpose of this study we exclude the use of audio features key, duration, and time signature.

**Table 1:** Snapshot of dataset containing tracks released in 2020

| danceability | energy | key | loudness | speechiness | acousticness | instrumentalness | liveness | valence | tempo   | duration_ms | time_signature | name                    | artist         | num_positive | num_negative | num_neutral | positivity  | negativity  | neutrality  | word_count | unique_word_count |
|--------------|--------|-----|----------|-------------|--------------|------------------|----------|---------|---------|-------------|----------------|-------------------------|----------------|--------------|--------------|-------------|-------------|-------------|-------------|------------|-------------------|
| 0.709        | 0.548  | 10  | -8.493   | 0.353       | 0.65         | 1.59E-06         | 0.133    | 0.543   | 83.995  | 160000      | 4              | What You Know Bout Love | Pop Smoke      | 7            | 2            | 33          | 0.166666667 | 0.047619048 | 0.785714286 | 209        | 130               |
| 0.799        | 0.66   | 1   | -6.153   | 0.079       | 0.256        | 0                | 0.111    | 0.471   | 140.04  | 195429      | 4              | Lemonade                | Internet Money | 8            | 15           | 34          | 0.140350877 | 0.263157895 | 0.596491228 | 307        | 177               |
| 0.514        | 0.73   | 1   | -5.934   | 0.0598      | 0.00146      | 9.54E-05         | 0.0897   | 0.334   | 171.005 | 200040      | 4              | Blinding Lights         | The Weeknd     | 3            | 10           | 22          | 0.085714286 | 0.285714286 | 0.628571429 | 150        | 75                |
| 0.65         | 0.613  | 9   | -6.13    | 0.128       | 0.00336      | 0                | 0.267    | 0.0804  | 149.972 | 194621      | 4              | Wishing Well            | Juice WRLD     | 0            | 22           | 30          | 0           | 0.423076923 | 0.576923077 | 238        | 104               |
| 0.737        | 0.802  | 0   | -4.771   | 0.0878      | 0.468        | 0                | 0.0931   | 0.682   | 144.015 | 172325      | 4              | positions               | Ariana Grande  | 10           | 5            | 33          | 0.208333333 | 0.104166667 | 0.6875      | 178        | 73                |
| 0.357        | 0.425  | 5   | -7.301   | 0.0333      | 0.584        | 0                | 0.322    | 0.27    | 102.078 | 198040      | 3              | Heather                 | Conan Gray     | 3            | 4            | 22          | 0.103448276 | 0.137931034 | 0.75862069  | 114        | 66                |
| 0.83         | 0.585  | 0   | -6.476   | 0.094       | 0.237        | 0                | 0.248    | 0.485   | 109.978 | 173711      | 4              | 34+35                   | Ariana Grande  | 3            | 13           | 52          | 0.044117647 | 0.191176471 | 0.764705882 | 249        | 127               |

### 4.3 Description of select data fields

The following terms defined are important in our analyses. In our data set most terms contain are represented by a value between 0 and 1, indicating least to most. For example, looking at the first two rows in *Table 1*, we can see that the track by the artist, Pop Smoke, has a greater speechiness score, indicating a greater percentage of that song contains spoken word. 
 
- **Danceability:** uses several musical elements (tempo, stability, beat strength, regularity) to determine how suitable a given track is for dancing
- **Energy:**  measures intensity of a song
- **Loudness:** a songs overall loudness measured in decibels
- **Speechiness:** identifies how much of a track contains spoken word
- **Acousticness:** confidence of a track being acoustic, or with physical instruments
- **Instrumentalness:** confidence of a track having no vocals
- **Liveness:** confidence of a track being a live recording
- **Valence:** predicts the overall happiness, or positivity of a track based on its musical features
- **Tempo:** the average beats per minute of a track
- **Positivity:** percentage of lines in a track's lyrics determined to have a positive sentiment score
- **Negativity:** percentage of lines in a track's lyrics determined to have a negative sentiment score
- **Neutrality:** percentage of lines in a track's lyrics determined to have a neutral sentiment score

Out of these fields, we seek to find which audio features correlate to a song's valence and if our positivity and negativity scores of a song's lyrics provide any meaningfulness in determining a song's positivity. For the purpose of this study we mainly focus on valence, energy, danceability, positivity, and negativity.

### 4.4 Preliminary Analysis of Data

When calculating averages of the feature fields captured in our dataset, we found it interesting that based on our lyrical interpretation, tracks between 2017 and 2020 tended to be more negative than positive. The average negativity score for a track in our dataset was 0.21 which means 21% of the lines in the track were deemed to have negative connotation, while having a 0.08 positivity score.

![Heatmap](https://github.com/cybertraining-dsc/fa20-523-341/raw/main/project/images/all_tracks_heatmap.png)

**Figure 1:** Heatmap of data with fields valence, energy, danceability, positivity, negativity

Backed by *Figure 1*, we find that track lyrics tend to be more negative than positive. However for the most part, even with tracks with negative lyrics, the valence, or overall happiness of the audio features hovers around 0.5; indicating that most songs tend to have neutral audio features. Looking at tracks with lyrics that are highly positive we find that the valence rises to about 0.7 to 0.8 and that songs with extremely high negatively also cause the valence to drop to the 0.3 range. These observations indicate that only extremes in lyrical sentiment correlate significantly in a song's valence, as some songs with negative lyrics may also be fast-tempo and energetic, keeping the valence relatively high compared to lyrical composition. This is shown in our visualization, where both tracks with positive and negative lyricals have high energy and danceability values, indicating fast-tempos and high-pitches.

### 4.5 Scatterplot Analysis

![Audio_Features_Scatterplots](https://github.com/cybertraining-dsc/fa20-523-341/raw/main/project/images/audio_features_scatterplots.png)

**Figure 2:** Scatterplots showing relation of features danceability, energy, speechiness, positivity, negativity, and neutrality to valence.

*Figure 2* describes the relation of several data fields we collected to a song's valence, or its overall positivity. We find that the positivity and negativity plots reflect that of the speechiness plot in that there seems to be little correlation between the x and y axes. On the other hand neutrality seems to show a positive correlation between a song's lyrical content and its respective valence. If a song is more neutral, it seems more likely to have a higher valence. 

![Spotify Distributions](https://github.com/cybertraining-dsc/fa20-523-341/raw/main/project/images/spotify_distributions.png)

**Figure 3:** Distributions of field values across the Spotify music library [^7].

Our scatterplots do show consistency with the expected distributions exemplified in the Spotify API documentation, as shown in *Figure 3*. In the top three plots, which use values for audio features obtained exclusively obtained from the audio features given by Spotify, we can see the these matching distributions which imply that most songs fall in the 0.4 to 0.8 range for danceability, energy, and valence, and 0 to 0.1 for speechiness. The low distribution in speechiness can be explained by music features being more dependant on instruments and sounds than spoken word. A track with higher than 0.33 speechiness score indicates that the track is very high in spoken word content over music, like a poetry recitation, talk show clip, etc [^7].

### 4.6 Linear and Polynomial Regression Analyses

We performed a simple linear regression test against valence with the audio and lyrical features described in *Figure 2* and *Figure 3*. Like the charts show, it was hard to find any linear correlation between the fields. *Table 2* displays the r-squared results that we obtained when applying linear regression to find the relationship between a song's feature and its valence. The only features that indicate potential relationships with a song's valence are energy, and danceability, as definitions of energy and and danceability indicate some semblance of positivity as well.

**Table 2:** R-Squared results obtained from linear regression application on select fields against valence

| Feature      | R-Squared     |
| ------------ | ------------- |
| Positivity   | -0.090859047 |
| Negativity   | -0.039686828 |
| Neutrality   | 0.093002783   |
| Energy       | 0.367113611   |
| Danceability | 0.324412662   |
| Speechiness  | 0.066492856   |

Since we found little relation between the selected features and valence, we tried applying polynomial regression with the same features as shown in *Table 3*. Again, we failed to find any relationship between a feature in our dataset and the song's valence. Energy and danceability once again were found to have the highest relationship with valence. We speculate that some of the data we have is misleading the regression applications; as mentioned before, we found some issues in reading sentiment in the lyrics we collected due to misspelled words, inaccurate punctuations, and non-english words.

**Table 3:** R-Square results obtained from polynomial regression application on select data fields against valence

| Feature      | R-Squared   |
| ------------ | ----------- |
| Positivity   | 0.013164307 |
| Negativity   | 0.001588184 |
| Neutrality   | 0.010308495 |
| Energy       | 0.136822113 |
| Danceability | 0.113119545 |
| Speechiness  | 0.008913925 |


### 4.7 Multivariate Regression Analysis

We performed multivariate regression tests to predict a song's valence with a training set of 5500 tracks and a test set of 551 tracks. Our first test only included four independent variables: neutrality, energy, danceability, and speechiness. Our second test included all numerical fields available in our data, adding loudness, acousticness, liveness, instrumentalness, tempo, positivity, word count, and unique word count to the regression coefficient calculations. In both tests we calculated the relative mean squared error (RMSE) between our predicted values and the actual values of a song's valence given several features. Our RMSEs were 0.1982 and 0.1905 respectively, indicating that as expected, adding additional pertinent independent variables gave slightly better results. However given that a song's valence is captured between 0 and 1.0, and both our RSMEs were approximately 0.19, it is unclear how significant the results of these tests are. *Figure 4* and *Figure 5* show the calculated differences between the predicted and actual values for the first 50 tracks in our testing dataset for each regression test respectively. 

![Multivariate Regression 1](https://github.com/cybertraining-dsc/fa20-523-341/raw/main/project/images/multivariate_regression_1.png)

**Figure 4:** Differences between expected and predicted values with application of multivariate regression model with 4 independent variables

![Multivariate Regression 2](https://github.com/cybertraining-dsc/fa20-523-341/raw/main/project/images/multivariate_regression_2.png)

**Figure 5:** Differences between expected and predicted values with application of multivariate regression model with 12 independent variables

## 5. Benchmarks

*Table 4* displays the benchmarks we received from key parts of our analyses. As expected, creating our dataset took a longer amount of time relative to the rest of the benchmarks. This is because accumulating the data involved sending two requests to online sources, and running the sentiment intensity analyzer on the lyrics received from the Genius API calls. Getting the sentiment of a line of text itself did not take much time at all. We found it interesting that applying multivariate regression on our dataset was much quicker than calculating averages on our dataset with numpy, and that it was the fastest process to complete.

**Table 4:** Benchmark Results

| Name                                                   | Status   |   Time |     Sum | Start               | tag   | Node         | User   | OS    | Version                             |
| ------------------------------------------------------ | -------- | ------ | ------- | ------------------- | ----- | ------------ | ------ | ----- | ----------------------------------- |
| Create dataset of 10 tracks                            | ok       | 12.971 | 168.523 | 2020-12-07 00:19:30 |       | 884e3d61f237 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| Sentiment Intensity Analyzer on a line of lyrical text | ok       |  0.001 |   0.005 | 2020-12-07 00:19:49 |       | 884e3d61f237 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| Load dataset                                           | ok       |  0.109 |   1.08  | 2020-12-07 00:19:59 |       | 884e3d61f237 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| Calculate averages of values in dataset                | ok       |  0.275 |   0.597 | 2020-12-07 00:19:59 |       | 884e3d61f237 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| Multivariate Regression Analysis on dataset            | ok       |  0.03  |   0.151 | 2020-12-07 00:21:49 |       | 884e3d61f237 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| Generate and display heatmap of data                   | ok       |  0.194 |   0.194 | 2020-12-07 00:20:03 |       | 884e3d61f237 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |
| Plot differences                                       | ok       |  0.504 |   1.473 | 2020-12-07 00:21:50 |       | 884e3d61f237 | collab | Linux | #1 SMP Thu Jul 23 08:00:38 PDT 2020 |

## 6. Conclusion

We received inconclusive results from our study. The linear and polynomial regression tests that we performed, showed little correlation between our lyrical features and a track's valence. This was backed by our multivariate regression test which performed with a RSME score of about 0.19 on our dataset. Since valence is recorded on a scale from 0 to 1.0, this means that our predictions typically fall within 20% of the actual value, which is considerably inaccurate. As previous studies have shown massive improvements in combining lyrical and audio features for machine learning applications in music, we believe that the blame for our low scores falls heavily on our approach to assigning sentiment scores on our lyrics [^1][^2]. Future studies should consider the presence of foreign lyrics and the potential inaccuracies of community submitted lyrics. 

There are several other elements of this study that could be improved upon in future iterations. In this project we only worked with songs released after the beginning of 2017, but obviously, people would still enjoy listening to songs from previous years. The Spotiy API contains audio features data for every song in its library, so it would be worth collecting that data on every song for usage in the generation of song recommendations. Secondly, our data set excluded songs on Spotify, whose lyrics could not be found easily on Genius.com. We should have handled these cases by attempting to find the lyrics from other popular websites which store music lyrics. And lastly, we worked with a very small dataset relative to the total amount of songs that exist, or that are available on Spotify. There is great possibility in repeating this study quite easily with a greater selection of songs. We were surprised by how small the file sizes were of our dataset of 6551 songs, the aggregated data set being only 2.3 megabytes in size. Using that value, a set of one million songs can be estimated to only be around 350 megabytes. 

## 7. Acknowledgements

We would like to give our thanks to Dr. Geoffrey Fox, Dr. Gregor von Laszewski, and the other associate instructors who taught FA20-BL-ENGR-E534-11530: Big Data Applications during the Fall 2020 semester at Indiana University, Bloomington for their suggestions and assistance in compiling this project report. Additionally we would like to thank the students who contributed to Piazza by either answering questions that we had ourselves, or giving their own suggestions and experiences in building projects. In taking this course we learned of several applications of and use cases for big data applications, and gained the knowledge to build our own big data projects.

## 8. References

[^1]: Hu, X., &amp; Downie, J. S. (2010). Improving mood classification in music digital libraries by combining lyrics and audio. Proceedings of the 10th Annual Joint Conference on Digital Libraries - JCDL '10. doi:10.1145/1816123.1816146

[^2]: Kashyap, N., Choudhury, T., Chaudhary, D. K., &amp; Lal, R. (2016). Mood Based Classification of Music by Analyzing Lyrical Data Using Text Mining. 2016 International Conference on Micro-Electronics and Telecommunication Engineering (ICMETE). doi:10.1109/icmete.2016.65

[^3]: Jeong, J. (2019, January 19). What Songs Tell Us About: Text Mining with Lyrics. Retrieved November 17, 2020, from https://towardsdatascience.com/what-songs-tell-us-about-text-mining-with-lyrics-ca80f98b3829

[^4]: Ahuja, S. (2019, September 25). Sort your music by any mood - Introducing moooodify. Retrieved November 17, 2020, from https://blog.usejournal.com/sort-your-music-by-any-mood-introducing-moooodify-41749e80faab

[^5]: Morris, C. (2016). SongSim. Retrieved November 17, 2020, from https://colinmorris.github.io/SongSim/

[^6]: Lamere, P. (2016, August 6). Organize Your Music. Retrieved November 17, 2020, from http://organizeyourmusic.playlistmachinery.com/

[^7]: Get Audio Features for a Track. (2020). Retrieved November 17, 2020, from https://developer.spotify.com/documentation/web-api/reference/tracks/get-audio-features/

[^8]: Genius API Documentation. (2020). Retrieved November 17, 2020, from https://docs.genius.com/
