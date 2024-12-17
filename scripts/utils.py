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

    def load_csv_files(self, folder_path):#load csv file from a folder
        """
        load csv file from a folder
        """
        self.data = pd.read_csv(folder_path)
        return self.data
    def get_data(self):
        self.data = yf.download(self.ticker,start = self.start_date, end = self.end_date, period='1d')
        return self.data
    def calculate_indicators_talib(data):#calculate indicators using talib
        data['sma_50'] = ta.SMA(data['Close'],timeperiod=50)#simple moving average
        data['sma_200'] = ta.SMA(data['Close'],timeperiod=200)#simple moving average
        data['rsi'] = ta.RSI(data['Close'],timeperiod=14)#relative strength index
        data['ema'] = ta.EMA(data['Close'],timeperiod=50)#exponential moving average
        # Unpack MACD values
        macd, signal, hist = ta.MACD(data['Close'], 
                                    fastperiod=12, 
                                    slowperiod=26, 
                                    signalperiod=9)
        data['macd'] = macd
        data['macd_signal'] = signal
        data['macd_hist'] = hist
        return data
    def calculatemetrics_pynance(ticker,start_date,end_date):
        data = yf.download(ticker, start=start_date, end=end_date)#get data from yfinance
        #calculate metrics
        data['sma_50'] = data['Close'].rolling(window=50).mean()#simple moving average
        data['sma_200'] = data['Close'].rolling(window=200).mean()#simple moving average
        data['rsi'] = data['Close'].rsi()#relative strength index
        data['ema'] = data['Close'].ema()#exponential moving average
        data['macd']= data['Close'].macd()#moving average convergence divergence
        return data
    def plot_data(self,data):
        plt.figure(figsize=(14,7))
        plt.plot(data['Close'],label='Close')
        plt.plot(data['sma_50'],label='SMA 50')
        plt.plot(data['sma_200'],label='SMA 200')
        plt.plot(data['rsi'],label='RSI')
        plt.plot(data['ema'],label='EMA')
        plt.plot(data['macd'],label='MACD')
        plt.legend()
        plt.show()



