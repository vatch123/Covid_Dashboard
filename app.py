from fetch import DataGenerator

import pandas as pd
import streamlit as st
import numpy as np
import altair as alt
import pydeck as pdk
import plotly.graph_objects as go
from datetime import date
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from plot_utils import plot_national_time_series

st.title('Covid 19 - India Analysis')
current_date = date.today()
current_date = current_date.strftime("%a, %d %b %Y")

some_text = '<p>Red</p><div class="box green">Green</div><div class="box blue">Blue</div>'

intro = '<span style="color:green">' + str(current_date) + '</span> <br>' + some_text
st.markdown(intro, unsafe_allow_html=True)

data_generator = DataGenerator()
current_national_data = data_generator.load_national_data()
current_national_data

cases_time_series = current_national_data['cases_time_series']
st.dataframe(cases_time_series)

analysis = st.radio("Choose type of analysis", ('Linear', 'Log'))
st.plotly_chart(plot_national_time_series(cases_time_series, analysis))


credits = "#### This app is created by Vatsalya Chaubey for easy visualization of the existing covid data in India"

