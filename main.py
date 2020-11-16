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

# Bollinger Bands (organized as lower, upper, middle)
returned_bands = abstract.BBANDS(data, price='Close')
bands = []
for i in range(len(returned_bands)):
	bands.append([
		returned_bands["lowerband"][i], 
		returned_bands["middleband"][i], 
		returned_bands["upperband"][i]
	])
data["BBANDS"] = bands

# Pivot Point + Support and Resistance (organized from lowest level to highest level)
data["Pivot"] = (data["High"] + data["Low"] + data["Close"])/3
support, resistance = [], []
for i in range(len(data)):
	support.append([
		2*data["Pivot"] - data["High"],
		data["Pivot"] - (data["High"] - data["Low"]),
		data["Low"] - 2*(data["High"] - data["Pivot"])
	])
	resistance.append([
		2*data["Pivot"] - data["Low"],
		data["Pivot"] + (data["High"] - data["Low"]),
		data["High"] + 2*(data["Pivot"] - data["Low"])
	])

data["Support"], data["Resistance"] = support, resistance

data = data[199:]