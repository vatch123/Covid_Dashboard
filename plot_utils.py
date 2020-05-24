from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import streamlit as st

def identity(x):
    return x

@st.cache
def plot_national_time_series(cases_time_series, analysis='Linear'):

    if analysis is 'Linear':
        func = identity
    elif analysis is 'Log':
        func = np.log10

    fig = make_subplots(rows=1,
                        cols=3,
                        )

    fig.add_trace(
        go.Scatter(
            x = cases_time_series.date,
            y = func(cases_time_series.totalconfirmed),
            fill='tozeroy',
            mode = 'lines',
            line_color = 'blue',
            fillcolor='lightblue',
            name = 'Total Confirmed',
        ),
        row=1, col=1
    )

    fig.add_trace(
        go.Scatter(
            x = cases_time_series.date,
            y = func(cases_time_series.totalrecovered),
            mode = 'lines',
            fill='tozeroy',
            line_color = 'green',
            fillcolor= 'lightgreen',
            name = 'Total Recovered',
        ),
        row=1, col=2
    )

    fig.add_trace(
        go.Scatter(
            x = cases_time_series.date,
            y = func(cases_time_series.totaldeceased),
            mode = 'lines',
            fill='tozeroy',
            line_color = 'red',
            fillcolor= 'palevioletred',
            name = 'Total Deceased',
        ),
        row=1, col=3
    )

    fig.update_layout(
        title={
            'text': "Coronavirus Cases - Daily Analysis (Linear Scale)",
            'y':0.85,
            'x':0.5,
            'xanchor': 'center',
            'yanchor': 'top'},
        yaxis_title="No. of cases",
        width=900,
        height=400,
        plot_bgcolor='rgb(255,255,255)',
        font=dict(
            family="Bold",
        )
    )

    return fig
