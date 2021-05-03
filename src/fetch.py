import pandas as pd
import streamlit as st

class DataGenerator:
    
    def __init__(self):
        super().__init__()
        self.base_url = "https://api.covid19india.org/"
        self.national_url = "data.json"
        self.states_url = "states_daily.json"
        self.district_latest_url = "state_district_wise.json"
        self.states_testing_url = "state_test_data.json"
    
    @st.cache
    def load_national_data(self):

        data_url = ''.join([self.base_url, self.national_url])
        national_data = pd.read_json(data_url, orient='index', convert_dates=True, date_unit='s')
        
        cases_time_series = pd.DataFrame(list(national_data.loc['cases_time_series',:]))

        # Taking care of the columns data types
        column_names = list(cases_time_series.columns)
        column_names.remove('date')
        column_names.remove('dateymd')
        cases_time_series[column_names] = cases_time_series[column_names].apply(pd.to_numeric)

        statewise_latest = national_data.loc['statewise',:].dropna()
        statewise_latest = pd.DataFrame(list(statewise_latest))
        statewise_latest = statewise_latest.drop(['statenotes'], axis=1)
        column_names = list(statewise_latest.columns)
        column_names.remove('lastupdatedtime')
        column_names.remove('state')
        column_names.remove('statecode')
        statewise_latest[column_names] = statewise_latest[column_names].apply(pd.to_numeric)
        statewise_latest = statewise_latest.drop(0)
        statewise_latest = statewise_latest.sort_values('confirmed', ascending=False)

        tested_time_series = national_data.loc['tested',:].dropna()
        tested_time_series = pd.DataFrame(list(tested_time_series))
        tested_time_series.updatetimestamp = pd.to_datetime(tested_time_series.updatetimestamp.str.split().str[0], dayfirst=True)

        data = {
            'cases_time_series': cases_time_series,
            'statewise_latest': statewise_latest,
            'tested_time_series' : tested_time_series,
        }

        return data
    

    @st.cache
    def load_district_latest_data(self):

        data_url = ''.join([self.base_url, self.district_latest_url])
        state_district = pd.read_json(data_url, orient='index', convert_dates=True, date_unit='s')

        return state_district

    
    @st.cache
    def load_states_timeseries(self):

        data_url = ''.join([self.base_url, self.states_url])
        states_timeseries = pd.read_json(data_url, orient='index', convert_dates=True, date_unit='s')
        states_timeseries = pd.DataFrame(list(states_timeseries.loc['states_daily',:]))

        return states_timeseries

    
    @st.cache
    def load_states_tests_timeseries(self):
        
        data_url = ''.join([self.base_url, self.states_testing_url])
        states_tests_timeseries = pd.read_json(data_url, orient='index', convert_dates=True, date_unit='s')
        states_tests_timeseries = pd.DataFrame(list(states_tests_timeseries.loc['states_tested_data',:]))

        return states_tests_timeseries

