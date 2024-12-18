from textblob import TextBlob
import pandas as pd
import matplotlib.pyplot as plt 

class CorrelationAnalyzer:
    def __init__(self):
        pass
    def sentiment_correlation(self, data):
       #read data
        
        
        # Normalize the date
        data['date'] = pd.to_datetime(data['date'], format='%Y-%m-%d', errors='coerce')
        data['date'] = data['date'].dt.tz_localize(None)
        
        # Only keep relevant columns: 'headline', 'date', and 'stock'
        data = data[['headline', 'date', 'stock']]
        
        # Sort the data by date
        data = data.sort_values('date')
        
        return data

    def get_sentiment(self, text):#sentiment of the text
        analysis = TextBlob(str(text))  # Convert to string and analyze
        return analysis.sentiment.polarity  # Returns value between -1 and 1

    def plot_sentiment_correlation(self, combined_data):
        #plot_sentiment_correlation
        plt.figure(figsize=(10, 6))
        plt.plot(combined_data['date'], combined_data['daily_return'], label='Daily Stock Returns', color='blue')
        plt.plot(combined_data['date'], combined_data['sentiment'], label='News Sentiment', color='orange')
        
        plt.title("Stock Returns vs News Sentiment Over Time")
        plt.xlabel("Date")
        plt.ylabel("Values")
        plt.legend()
        plt.grid()
        plt.show()

    def sentiment_stock_analysis(self, datafile):
            # Preprocess the data
        data = self.sentiment_correlation(datafile)

        # Sentiment analysis
        data['sentiment'] = data['headline'].apply(self.get_sentiment)
        daily_sentiment = data.groupby('date')['sentiment'].mean().reset_index()

        # Calculate daily stock returns
        data['daily_return'] = data['stock'].pct_change()
        data = data.dropna(subset=['daily_return'])

        # Merge sentiment and stock data on 'date'
        combined_data = pd.merge(data[['date', 'daily_return']], daily_sentiment, on='date', how='inner')

        # Calculate correlation
        correlation = combined_data['daily_return'].corr(combined_data['sentiment'])
        print(f"Correlation between news sentiment and daily stock returns: {correlation:.2f}")
        
        # Return the results
        return correlation, combined_data
