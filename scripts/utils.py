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

    def load_csv_files(self,ticker, folder_path):
        """
        load csv file from a folder
        """
        file_name = f"{ticker.lower()}_historical_data.csv"  # Adjust the file naming pattern if needed
        file_path = os.path.join(folder_path, file_name)
        self.data = pd.read_csv(file_path)
        return self.data
    def get_data(self):
        self.data = yf.download(self.ticker,start = self.start_date, end = self.end_date, period='1d')
        return self.data
    def calculate_indicators_talib(self,data,window):#calculate indicators using talib
        data['sma_50'] = ta.SMA(data,timeperiod=window)#simple moving average
        data['sma_200'] = ta.SMA(data,timeperiod=200)#simple moving average
        data['rsi'] = ta.RSI(data,timeperiod=14)#relative strength index
        data['ema'] = ta.EMA(data,timeperiod=200)#exponential moving average
        data['macd'] = ta.MACD(data,fastperiod=12,slowperiod=26,signalperiod=9)#moving average convergence divergence
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



