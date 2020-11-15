import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from talib import abstract

ticker = "AMZN"
# period param = period you want + 200d
data = yf.Ticker(ticker).history(period="452d").dropna()

# SMA
data["SMA10"] = data["Close"].rolling(10).mean()
data["SMA20"] = data["Close"].rolling(20).mean()
data["SMA50"] = data["Close"].rolling(50).mean()
data["SMA200"] = data["Close"].rolling(200).mean()

# EMA
data["EMA10"] = data["Close"].ewm(span=10, adjust=False).mean()
data["EMA20"] = data["Close"].ewm(span=20, adjust=False).mean()
data["EMA50"] = data["Close"].ewm(span=50, adjust=False).mean()
data["EMA200"] = data["Close"].ewm(span=200, adjust=False).mean()

# RSI
data["RSI"] = abstract.RSI(data, timeperiod=14, price='Close')

# MACD
returned_macd = abstract.MACDFIX(data, price='Close')
data["MACD"] = returned_macd["macd"]
data["MACDSignal"] = returned_macd["macdsignal"]
data["MACDHist"] = returned_macd["macdhist"] 

data = data[199:]

# plt.plot(data.index, data["Close"]) -> plots historical closing data
# plt.show() -> shows plot