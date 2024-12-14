import pandas as pd
import numpy as np
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
#function to read the csv file
def read_csv_file(file_path):
    #read the file
    data=pd.read_csv(file_path)
    #remove unnamed columns
    cols_with_missing = [col for col in data.columns if 'unnamed' in col.lower()]
    data = data.drop(cols_with_missing,axis=1)
    #get additional infos
    column_names = data.columns.tolist()
    row_count=data.shape[0]
    #remove missing values
    #data = data.dropna()
    #return the data
    return {"data":data,
    "column_names":column_names,
    "row_count":row_count}
def count_headline_length(data):
    #get the length of the headline
    data_headline = data['headline']
    length = [len(str(headline)) for headline in data_headline]
    #calculate the mean,median,stdev,length_counts
    mean = np.mean(length)
    median_length = np.median(length)
    stdev_length = np.std(length)
    length_counts=len(length)
    
    return {
        "mean": mean,
        "median_length": median_length,
        "stdev_length": stdev_length,
        "length": length_counts
    }#return the values in a dictionary form
#function to analyze the sentiment of the text
def analyze_sentiment(text):
    blob = TextBlob.polarity_scores(text)
    #return the sentiment scores
    return {'polarity': blob.sentiment.polarity}
            #polarity is a measure of the sentiment of the text (-1 to 1)
#add sentiment category to the dataframe
def get_sentiment_category(score):
    if score > 0:
        return 'positive'
    elif score < 0:
        return 'negative'
    else:
        return 'neutral'









