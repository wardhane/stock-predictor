import streamlit as st 
from datetime import date
import yfinance
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

st.title('Stock :bow_and_arrow: Series Forecasting with Prophet')
