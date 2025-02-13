!pip install streamlit prophet plotly
import streamlit as st
from prophet import Prophet
from prophet.plot import plot_plotly
import plotly.offline as py
import yfinance
import pandas as pd
import numpy as np
