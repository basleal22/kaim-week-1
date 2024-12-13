import pandas as pd
import numpy as np
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
def count_headline_length(data,mean,median_length, stdev_length,length):
    #get the length of the headline
    data=data['headline']
    length=[len(data) for data in data]
    #calculate the mean,median,stdev
    mean=np.mean(length)
    average_length=np.array(length)
    median_length = np.median(length)
    stdev_length=np.std(length)
    return {"average_length":average_length,"mean":mean,
    "median_length":median_length,
    "stdev_length":stdev_length,
    "length":length}#return the values in a dictionary form
    




