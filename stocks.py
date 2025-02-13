import streamlit as st
from prophet import Prophet
from prophet.plot import plot_plotly
import plotly.offline as py
import yfinance
import pandas as pd
import numpy as np

st.title('Stock :bow_and_arrow: Series Forecasting with Prophet')
