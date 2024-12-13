import pandas as pd
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




