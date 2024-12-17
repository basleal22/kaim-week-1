import pandas as pd
import numpy as np
from textblob import TextBlob
import matplotlib.pyplot as plt
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
    blob = TextBlob(str(text))
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
#find common phrases in the text
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
def common_phrases(text):
    text = str(text).lower()
    #most common phrases in the text
    phrases=['fda approval','fda approval for', 'fda approval to', 'fda approval of',
             'price target','stock split','earnings report','earnings','market share','fda','stock']
    #store most common phrases in a list called 'phrase'
    found_phrases= [phrase for phrase in phrases if phrase in text]
    return found_phrases
def timeseries_analysis(data):
    data['date'] =pd.to_datetime(data['date'])
    data.set_index('date',inplace=True) #set the date as the index
    #resample the data by month and count number of articles per month
    monthly_counts = data.resample('M').size()
    plt.figure(figsize=(10,6))
    monthly_counts.plot()
    plt.title('Number of articles per month')
    plt.xlabel('date')
    plt.ylabel('number of articles')
    plt.grid(True)
    plt.show()
    return monthly_counts
def spike_analysis(data):#detect spikes in the data using moving average
    monthly_counts = data.resample('M').size()
    #calculate the moving average
    monthly_moving_average = monthly_counts.rolling(window=7).mean()
    #plot the data and the moving average
    plt.figure(figsize=(10,6))
    monthly_counts.plot()
    monthly_moving_average.plot()
    plt.title('Number of articles per month')
    plt.xlabel('date')
    plt.ylabel('number of publications')
    plt.grid(True)
    plt.show()
    threshold = monthly_counts.quantile(0.95)#top 5% of the data
    spikes = monthly_counts[monthly_counts> threshold]
    print(spikes)
    return monthly_counts,monthly_moving_average
def plot_spikes(data):
    monthly_counts,monthly_moving_average = spike_analysis(data)
    plt.figure(figsize=(10,6))
    monthly_counts.plot()
    monthly_moving_average.plot()
    plt.title('Number of articles per month')
    plt.xlabel('date')
    plt.ylabel('number of publications')
    plt.grid(True)
    plt.show()













