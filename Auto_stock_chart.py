import pandas as pd
import numpy as np
import pandas_datareader as web
from datetime import datetime
from datetime import timedelta
from matplotlib import pyplot as plt

# set time range for the last 180 days
end_date = datetime.now()
start_date = end_date - timedelta(days = 180)
# initialize the list of stock symbols
symbols = []

try:
    def main():
        res = 'y'
        print("Beginning...")
        while res == 'y':
            stock = input("Enter the stock symbol you want to see: \n> ").upper()
            symbols.append(stock)
            while True:
                res = input("Would you want to see any other stock? [y/n] \n> ")
                if res == 'y' or res == 'n':
                    break
        for symbol in symbols:
            price_chart(symbol)
        
    def price_chart(symbol):
        """Price chart of stock symbols that user wants to see, for the last 180 days"""
        stock_data = web.get_data_yahoo(symbol, start_date, end_date)
        stock_data_closing_price = stock_data['Adj Close']    
        stock_data_closing_price.plot()
        plt.legend(symbols)
        plt.xlabel("Date")
        plt.ylabel("Closing Price")
        plt.title("Stock Price for the last 180 days, updated at " + str(datetime.now()))
        plt.grid()
    
    for symbol in symbols:
        price_chart(symbol)
    
    def index_chart():
        """Price chart of the Dow Jones, Nasdaq and S&P500 for the last 180 days"""
        index = ['DJIA', '^GSPC', '^IXIC']
        index_data = web.get_data_yahoo(index, start_date, end_date)
        index_data_closing_price = index_data['Adj Close']
        plt.figure(figsize=(12,10))
        plt.suptitle('Market Index for the last 180 days')
        plt.subplot(3,1,1)
        index_data_closing_price['DJIA'].plot(color = 'blue')
        plt.title('Dow 30')
        plt.xlabel('')
        plt.grid()
        
        plt.subplot(3,1,2)
        index_data_closing_price['^GSPC'].plot(color = 'blue')
        plt.title("SP500")
        plt.xlabel('')
        plt.grid()
        
        plt.subplot(3,1,3)
        index_data_closing_price['^IXIC'].plot(color = 'blue')
        plt.title("NASDAQ")
        plt.xlabel('')
        plt.grid()
        plt.tight_layout(pad = 3.2)
        #plt.show()
    index_chart()
    while True:
        plt.show()
        main()

except:
    main()
