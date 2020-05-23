from fetch import DataGenerator

import pandas as pd
import streamlit as st
import numpy as np
import altair as alt
import pydeck as pdk
import plotly.graph_objects as go
from datetime import date
import matplotlib

st.title('Covid 19 - India Analysis')
current_date = date.today()
current_date = current_date.strftime("%a, %d %b %Y")

intro = '<span style="color:green">' + str(current_date) + '</span>'
st.markdown(intro, unsafe_allow_html=True)

data_generator = DataGenerator()
current_national_data = data_generator.load_national_data()
current_national_data

case_time_series = current_national_data['case_time_series']
case_time_series

import plotly.express as px
fig = px.area(case_time_series, x='date', y='totalconfirmed')
st.plotly_chart(fig)

figure = go.Figure()
figure.add_trace(
    go.Scatter(
        x = case_time_series.date,
        y = case_time_series.totalconfirmed,
        fill='tozeroy',
        mode = 'lines',
        line_color = 'blue',
        fillcolor='lightblue',
        name = 'Total Confirmed',
    )
)

figure.add_trace(
    go.Scatter(
        x = case_time_series.date,
        y = case_time_series.totalrecovered,
        mode = 'lines',
        fill='tozeroy',
        line_color = 'green',
        fillcolor= 'lightgreen',
        name = 'Total Recovered',
    )
)

figure.add_trace(
    go.Scatter(
        x = case_time_series.date,
        y = case_time_series.totaldeceased,
        mode = 'lines',
        fill='tozeroy',
        line_color = 'red',
        fillcolor= 'palevioletred',
        name = 'Total Deceased',
    )
)

figure.update_layout(
    title={
        'text': "Coronavirus Cases - Daily Analysis",
        'y':0.85,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'},
    yaxis_title="No. of cases",
    xaxis_title="Date",
    annotations=[
        dict(
            text="Source: covid19india.org",
            showarrow=False,
            xref="paper",
            yref="paper",
            x=0,
            y=0)
    ]
)

st.plotly_chart(figure)


credits = "#### This app is created by Vatsalya Chaubey for easy visualization of the existing covid data in India"