import yfinance as yf
import pandas as pd
import talib as ta
import os
import pynance as pn
import numpy as np
import matplotlib.pyplot as plt
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
    def calculate_indicators_talib(self,data,window):#calculate indicators using talib
        data['sma_50'] = ta.SMA(data,timeperiod=window)
        data['sma_200'] = ta.SMA(data,timeperiod=200)
        data['rsi'] = ta.RSI()
        data['ema'] = ta.EMA()
        data['macd'] = ta.MACD()
        return data
    def calculatemetrics_pynance(self,ticker,start_date,end_date):
        data = pn.get_data(ticker,start_date,end_date)#get data from pynance
        #calculate metrics
        data['sma_50'] = data['close'].rolling(window=50).mean()#simple moving average
        data['sma_200'] = data['close'].rolling(window=200).mean()#simple moving average
        data['rsi'] = data['close'].rsi()#relative strength index
        data['ema'] = data['close'].ema()#exponential moving average
        data['macd']= data['close'].macd()#moving average convergence divergence
        return data
    def plot_data(self,data):
        plt.figure(figsize=(14,7))
        plt.plot(data['close'],label='Close')
        plt.plot(data['sma_50'],label='SMA 50')
        plt.plot(data['sma_200'],label='SMA 200')
        plt.plot(data['rsi'],label='RSI')
        plt.plot(data['ema'],label='EMA')
        plt.plot(data['macd'],label='MACD')
        plt.legend()
        plt.show()



