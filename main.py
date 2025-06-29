import pandas as pd
import numpy as np
import yfinance as yf
import pandas_ta as ta
import matplotlib.pyplot as plt


end_date = '2025-06-27'
start_date = '2023-06-07'
stock = 'BLK'

df = yf.download(tickers=stock,start=start_date,end=end_date,auto_adjust=True)
df.columns = df.columns.get_level_values(0)
df.columns = df.columns.str.lower()


def moving_avg(window):
    df['moving avg'] = df['close'].rolling(window=window).mean()
    return df

def trade(df):
    position = 0
    cash = 10000
    shares = 0

    for i in range(len(df)):
        close_price = df['close'].iloc[i]
        moving_average = df['moving avg'].iloc[i]

        if position == 0 and close_price > moving_average:
            shares = cash // close_price
            cash -= shares * close_price
            position = 1
            print(f"Bought {shares} shares at {close_price} on {df.index[i].date()}")

        elif position == 1 and close_price < moving_average:
            cash += shares * close_price
            print(f"Sold {shares} shares at {close_price} on {df.index[i].date()}")
            shares = 0
            position = 0
    print(f"End cash balance: {cash}")
    
df = moving_avg(20)
trade(df)
        
    


