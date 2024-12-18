from textblob import TextBlob
import pandas as pd
import numpy as np
class correlation_analyer:
    def __init__(self,ticker,start_date,end_date):
        self.ticker=ticker
        self.start_date=start_date
        self.end_date=end_date
    def get_sentiment(data):
        analysis=TextBlob(str(data))
        return analysis.sentiment.polarity
    