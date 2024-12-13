import pandas as pd
from matplotlib import pyplot as plt
def plot_stock_data(data,date_column, stock_value_column,title):
    #plots stock value over time
    data = data.copy()
    plt.figure(figsize=(10,6))
    #here the date_column is the x axis and the stock_value_column is the y axis
    plt.plot(data[date_column],data[stock_value_column],label=stock_value_column,color='blue')
    plt.title(title)
    plt.xlabel(date_column)
    plt.ylabel(stock_value_column)
    plt.legend()
    plt.grid(True)
    plt.show()
    return plt.gcf()
