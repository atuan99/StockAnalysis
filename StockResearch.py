import pandas_datareader as web
import pandas as pd
from datetime import datetime
from matplotlib import pyplot as plt
import requests
import json

try:
    def get_date():
        year = input("Enter the starting year: ")
        start = datetime(int(year), 1,1)
        end = datetime.today()
        return start, end
    
    def create_price_and_volume_chart(symbol):
        start_date, end_date = get_date()
        stock = web.get_data_yahoo(symbol, start_date, end_date)
        stock_close_price = stock['Adj Close']
        stock_volume = stock['Volume']
        fig, ax1 = plt.subplots()
        ax2 = ax1.twinx()
        stock_close_price.plot(ax = ax1, color = 'g', label = 'Price', legend = 'Price')
        #ax1.set_facecolor('grey')
        plt.suptitle('Price and Volume of ' + str(symbol))
        plt.ylabel('Price')
        ax1.grid(color = 'black')
        stock_volume.plot(ax = ax2, color = 'b', alpha = 0.2, label = 'Volume', legend = 'Volume')
        plt.yticks([])
        plt.ylabel('Volume')
        plt.show()
    
    def create_moving_average(symbol):
        start_date, end_date = get_date()
        stock = web.get_data_yahoo(symbol, start_date, end_date)
        #stock['MA10'] = stock['Open'].rolling(10).mean()
        #stock['MA20'] = stock['Open'].rolling(20).mean()
        stock['MA50'] = stock['Adj Close'].rolling(50).mean()
        #stock['MA100'] = stock['Open'].rolling(100).mean()
        stock['MA200'] = stock['Adj Close'].rolling(200).mean()
        stock[['Adj Close', 'MA50', 'MA200']].plot()
        plt.title('Price and Moving Average of ' + symbol)
        plt.xlabel('Price')
        plt.grid()
        plt.show()
    
    def create_daily_return_chart(symbol):
        start_date, end_date = get_date()
        stock = web.get_data_yahoo(symbol, start_date, end_date)
        stock_daily_returns = stock['Adj Close'].pct_change()
        stock_daily_returns.plot(color = 'g')
        plt.title('Daily Returns of ' + str(symbol))
        plt.ylabel('Daily Returns')
        plt.grid()
        plt.show()
    
    def get_company_rating(symbol):
        fr = requests.get(f'https://financialmodelingprep.com/api/v3/company/rating/{symbol}')
        fr = fr.json()
        ratings = fr['rating']
        ratings_details = fr['ratingDetails']
        ratings_df = pd.DataFrame(list(ratings.items()), columns = ['Rating', symbol])
        ratings_details_df = pd.DataFrame(list(ratings_details.items()), columns = ['Rating', symbol])
        ratings_total = [ratings_df, ratings_details_df]
        ratings_concat = pd.concat(ratings_total)
        return ratings_concat        
    
    def get_company_financial_ratios(symbol):
        fr = requests.get(f'https://financialmodelingprep.com/api/v3/financial-ratios/{symbol}')
        fr = fr.json()
        investment = fr['ratios'][0]['investmentValuationRatios']
        profitability = fr['ratios'][0]['profitabilityIndicatorRatios'] 
        operating = fr['ratios'][0]['operatingPerformanceRatios'] 
        liquidity = fr['ratios'][0]['liquidityMeasurementRatios']
        debt = fr['ratios'][0]['debtRatios']
        cashflow = fr['ratios'][0]['cashFlowIndicatorRatios']
    
        investment = pd.DataFrame(list(investment.items()), columns = ['Ratios', symbol])
        profitability = pd.DataFrame(list(profitability.items()), columns = ['Ratios', symbol])
        operating = pd.DataFrame(list(operating.items()), columns = ['Ratios', symbol])
        liquidity = pd.DataFrame(list(liquidity.items()), columns = ['Ratios', symbol])
        debt = pd.DataFrame(list(debt.items()), columns = ['Ratios', symbol])
        cashflow = pd.DataFrame(list(cashflow.items()), columns = ['Ratios', symbol])
        total = [investment, profitability, operating, liquidity, debt, cashflow]
        total_concat = pd.concat(total)
        return total_concat
    
    def get_company_profile(symbol):
        fr = requests.get(f'https://financialmodelingprep.com/api/v3/company/profile/{symbol}')
        fr = fr.json()
        profile = fr['profile']
        profile_df = pd.DataFrame(list(profile.items()), columns = ['Profile', symbol])
        return profile_df
    
    def main():
        print("Program begins...\n ")
        print("Available options: \n[1] for Price & Volume chart \n[2] for Moving Average chart \n[3] for Daily Return chart \n[4] for Analyst Rating \n[5] for Company's financial ratios \n[6] for Company's Profile")
        symbol = input("Type in the stock ticker: \n> ")
        option = int(input("Choose the option from the above instructions: \n> "))
        while True:
            if option == 1:
                create_price_and_volume_chart(symbol.upper())
                print("Available options: \n[1] for Price & Volume chart \n[2] for Moving Average chart \n[3] for Daily Return chart \n[4] for Analyst Rating \n[5] for Company's financial ratios \n[6] for Company's Profile")
                symbol = input("Type in the stock ticker: \n> ")
                option = int(input("Choose the option from the above instructions: \n> "))
                #plt.show()
            elif option == 2:
                create_moving_average(symbol.upper())
                print("Available options: \n[1] for Price & Volume chart \n[2] for Moving Average chart \n[3] for Daily Return chart \n[4] for Analyst Rating \n[5] for Company's financial ratios \n[6] for Company's Profile")
                symbol = input("Type in the stock ticker: \n> ")
                option = int(input("Choose the option from the above instructions: \n> "))
                #plt.show()
            
            elif option == 3:
                create_daily_return_chart(symbol.upper())
                print("Available options: \n[1] for Price & Volume chart \n[2] for Moving Average chart \n[3] for Daily Return chart \n[4] for Analyst Rating \n[5] for Company's financial ratios \n[6] for Company's Profile")
                symbol = input("Type in the stock ticker: \n> ")
                option = int(input("Choose the option from the above instructions: \n> "))
                #plt.show()
            elif option == 4:
                x = get_company_rating(symbol.upper())
                print(x)
                print("Available options: \n[1] for Price & Volume chart \n[2] for Moving Average chart \n[3] for Daily Return chart \n[4] for Analyst Rating \n[5] for Company's financial ratios \n[6] for Company's Profile")
                symbol = input("Type in the stock ticker: \n> ")
                option = int(input("Choose the option from the above instructions: \n> "))   
            elif option == 5:
                x = get_company_financial_ratios(symbol.upper())
                print(x)
                print("Available options: \n[1] for Price & Volume chart \n[2] for Moving Average chart \n[3] for Daily Return chart \n[4] for Analyst Rating \n[5] for Company's financial ratios \n[6] for Company's Profile")
                symbol = input("Type in the stock ticker: \n> ")
                option = int(input("Choose the option from the above instructions: \n> "))
            elif option == 6:
                x = get_company_profile(symbol.upper())
                print(x)
                print("Available options: \n[1] for Price & Volume chart \n[2] for Moving Average chart \n[3] for Daily Return chart \n[4] for Analyst Rating \n[5] for Company's financial ratios \n[6] for Company's Profile")
                symbol = input("Type in the stock ticker: \n> ")
                option = int(input("Choose the option from the above instructions: \n> "))  
            else:
                print("Available options: \n[1] for Price & Volume chart \n[2] for Moving Average chart \n[3] for Daily Return chart \n[4] for Analyst Rating \n[5] for Company's financial ratios \n[6] for Company's Profile")
                symbol = input("Type in the stock ticker: \n> ")
                option = int(input("Choose the option from the above instructions: \n> "))
    
    main()
except:
    print("Error or information not found. Program restarting... \n ")
    main()
    
