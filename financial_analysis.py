import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px

st.write("""
# Simple Stock Price App by Pascal

Shown are the stock closing price and volume of Google!

""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

# Additional Charts
# -----------------

# Moving Average Lines (50-day and 200-day)
st.subheader("Moving Averages")
st.line_chart(tickerDf['Close'].rolling(window=50).mean())
st.line_chart(tickerDf['Close'].rolling(window=200).mean())
