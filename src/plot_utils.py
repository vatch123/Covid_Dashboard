from plotly.subplots import make_subplots
import plotly.graph_objects as go
import numpy as np
import streamlit as st
import plotly.express as px
import pandas as pd

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
            'text': "Coronavirus Cases - Daily Analysis ("+ analysis + " Scale)",
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

@st.cache
def plot_last_ten_days(cases_time_series):

    fig = go.Figure()

    fig.add_trace(
            go.Bar(
                x = cases_time_series.date[-10:],
                y = cases_time_series.dailyconfirmed[-10:],
                marker_color='darkcyan',
                name = 'Daily Confirmed',
                insidetextanchor='end',
            ),
        )

    fig.add_trace(
            go.Bar(
                x = cases_time_series.date[-10:],
                y = cases_time_series.dailyrecovered[-10:],
                marker_color='lightgreen',
                name = 'Daily Recovered',
            ),
        )

    fig.add_trace(
            go.Bar(
                x = cases_time_series.date[-10:],
                y = cases_time_series.dailydeceased[-10:],
                marker_color='red',
                name = 'Daily Deceased',
                insidetextanchor='end',
            ),
        )

    fig.update_layout(
            title={
                'text': "Coronavirus Cases: Changes in last 10 days",
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
            ),
            barmode = 'group',
            bargap=0.15,
            bargroupgap=0.1,
        )
    
    return fig


@st.cache
def plot_state_data(refined_data):

    fig = px.bar(refined_data, x="confirmed", y="state", color='state', orientation='h',
            hover_data=["active", "recovered", 'deaths', 'lastupdatedtime'],
            text='confirmed',
            opacity=1,
            color_discrete_sequence=px.colors.qualitative.Pastel,
            )

    fig.update_layout(
                title={
                    'text': "States with most confirmed cases",
                    'y':0.9,
                    'x':0.5,
                    'xanchor': 'center',
                    'yanchor': 'top'},
                yaxis_title="States",
                xaxis_title='Confirmed cases',
                width=900,
                height=400,
                plot_bgcolor='rgb(255,255,255)',
                font=dict(
                    family="Bold",
                ),
            )
    
    return fig


@st.cache(allow_output_mutation=True)
def plot_testing_data(tested_time_series):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
                                x = tested_time_series.updatetimestamp,
                                y = tested_time_series.totalsamplestested,
                                mode = 'lines+markers',
                                line_color='green',
                                connectgaps=True,
                            )
                )

    fig.update_layout(
            title={
                'text': "<b> Tests Conducted all over India </b>",
                'y':0.85,
                'x':0.5,
                'xanchor': 'center',
                'yanchor': 'top'},
            yaxis_title="No. of tests conducted",
            width=900,
            height=400,
            plot_bgcolor='rgb(255,255,255)',
            font=dict(
                family="Bold",
            )
        )
    
    return fig

