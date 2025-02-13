import streamlit as st 
import appdirs as ad
ad.user_cache_dir = lambda *args: "/tmp"

from datetime import date
import yfinance
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

st.title('Stock :bow_and_arrow: Series Forecasting with Prophet')

