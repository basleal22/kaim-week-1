import yfinance as yf
import pandas as pd
import talib as ta
import os
class financial_analyzer:
    def __init__(self,ticker,start_date,end_date):
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date

    def load_csv_files(self, folder_path):
        """
        Load all CSV files from a folder into a dictionary of DataFrames.
        :param folder_path: Path to the folder containing CSV files
        :return: Dictionary of DataFrames, where the key is the file name (ticker)
        """
        dataframes = {}
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.csv'):
                ticker = file_name.split('.')[0]  # Extract the ticker from the file name
                file_path = os.path.join(folder_path, file_name)  # Full file path
                dataframes[ticker] = pd.read_csv(file_path)
                print(f"Loaded data for {ticker} from {file_name}")
        return dataframes
    def get_data(self):
        self.data = yf.download(self.ticker,start = self.start_date, end = self.end_date, period='1d')
        return self.data
    def calculate_moving_average(self,data,window):
        return ta.SMA(data,timeperiod=window)
        self.data.to_csv(f'{ticker}.csv')


