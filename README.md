### Text-Mining-Group-Project
Tom, Yop, Nick

Title - Modern Family character analysis utilising text mining methods.

Abstract:

We utilised classic text mining techniques to extract data from transcripts of the popular TV sitcom Modern Family. After cleaning the data we then performed several analyses on word frequencies and sentiments, making use of the general sentiment analysis model we trained using a large (1.6M+) dataset of tweets. Finally, we illustrated our results through the use of various graphs and wordclouds.

The Transcripts are compiled into several CSV files seperated by season, after removing all lines not stated by the main cast, then normalizing and semmatizing them. Then the Character Name, and the Line, Normalized Line and Semmatized Line are all placed in a row for processing.


Potential Additions:
- Character Analysis
  - Per Character, we can see their most common words and see how they've fluctuated throughout the airing of the show.
  - We can additionally use general sentiment analysis to see how 'positive' or 'negative' each character is based upon their words spoken.


Research gap:
- We have found limited NLP and sentiment analysis research conducted on TV shows, with only the shows Friends and The Simpsons previously explored. 

Research questions:

- Can we utilize classic text-mining Techniques to conduct analysis on characters of the show Modern Family?
- Does this provide us with a somewhat accurate undestanding of the characters?

Datasets:

- Modern Family Transcripts

- Twitter Sentiment Analysis Training Sets

Documentation

### Before running the code_for_data.pynb file
Install pickle, wordlcoud and seaborn libraries.

### Before running the Sentiment Analysis.pynb file
Install opendatasets library (pip install opendatasets), then everything else should work fine.

Be sure to have a Kaggle account set up before running the notebook.

