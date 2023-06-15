import time
import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st


# read csv from a URL
py_path = 'EDA\Simona\tests\st_dashboard.py'
df_path = 'EDA/Simona/tests/Preprocessed_Dataset.csv'

df = pd.read_csv(df_path, index_col=0)
st.title("Real-Time / Live Data Science Dashboard")
