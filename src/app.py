from fetch import DataGenerator

import pandas as pd
import streamlit as st
import plotly.graph_objects as go
from datetime import date
from plotly.subplots import make_subplots
import plotly.graph_objects as go
from plot_utils import *

st.title('Covid 19 - India Analysis')
current_date = date.today()
current_date = current_date.strftime("%a, %d %b %Y")

intro = '<span style="color:green">' + str(current_date) + '</span> <br>'
st.markdown(intro, unsafe_allow_html=True)
st.markdown('### Latest Updates')


data_generator = DataGenerator()
current_national_data = data_generator.load_national_data()

cases_time_series = current_national_data['cases_time_series']

intro = '***Total Confirmed Cases***: <span style="color:blue">' + str(list(cases_time_series['totalconfirmed'])[-1]) + '&nbsp&nbsp&nbsp&nbsp&nbsp+' + str(list(cases_time_series['dailyconfirmed'])[-1]) + '</span><br>'
intro += '***Total Recovered Cases***: <span style="color:green">' + str(list(cases_time_series['totalrecovered'])[-1]) + '&nbsp&nbsp&nbsp&nbsp&nbsp+' + str(list(cases_time_series['dailyrecovered'])[-1]) + '</span> <br>'
intro += '***Total Deceased Cases***: <span style="color:red">' + str(list(cases_time_series['totaldeceased'])[-1]) + '&nbsp&nbsp&nbsp&nbsp&nbsp+' + str(list(cases_time_series['dailydeceased'])[-1]) + '</span> <br>'
intro += '***Ratio of Recovered to Deceased Cases***: <span style="color:green">' + str(round(list(cases_time_series['totalrecovered'])[-1]/list(cases_time_series['totaldeceased'])[-1],2)) +'</span> : <span style="color:red">1</span><br>'
st.markdown(intro, unsafe_allow_html=True)

analysis = st.radio("Choose type of analysis", ('Linear', 'Log'))
st.plotly_chart(plot_national_time_series(cases_time_series, analysis))

st.plotly_chart(plot_last_ten_days(cases_time_series))


statewise_latest = current_national_data['statewise_latest']

states = st.multiselect(
                        label='Select the states', 
                        options=statewise_latest['state'].to_list(), 
                        default=statewise_latest['state'].to_list()[:5],
                        )
refined_data = statewise_latest.loc[statewise_latest['state'].isin(states)]

st.plotly_chart(plot_state_data(refined_data))

tested_time_series = current_national_data['tested_time_series']

st.plotly_chart(plot_testing_data(tested_time_series))

data_credits = "#### The data used in this app has been collected by 'Covid19 India'. The link to the original data [api](https://api.covid19india.org/). The app uses the data from that source as it without any claims to the ownership or authencity of the data."

credits = "<br>This app is created by [Vatsalya Chaubey](www.linkedin.com/in/vatsalya-chaubey) for easy visualization of the existing covid data in India"

st.markdown(data_credits)
st.markdown(credits, unsafe_allow_html=True)
