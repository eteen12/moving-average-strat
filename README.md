# Moving Average Trading Bot

Python trading bot that uses a moving average crossover strat on equity price data.
Donwloads histroical data and calculates a moving a moving average in order to compute when to buy and sell.

![image](https://github.com/user-attachments/assets/8a4d3491-dbd8-49c0-97f9-96fb8c9ef04c)


## Basic Logic

- Buy when the closing price crosses above the moving average
- Sell when the closing price crosses below the moving average
- Tracks cash balance and shares held
- Prints trade actions and final cash balance

## Req's

`pip install pandas numpy yfinance pandas_ta matplotlib notebook`
