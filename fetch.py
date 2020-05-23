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

        statewise_latest = national_data.loc['statewise',:].dropna()
        statewise_latest = pd.DataFrame(list(statewise_latest))

        tested_time_series = national_data.loc['tested',:].dropna()
        tested_time_series = pd.DataFrame(list(tested_time_series))

        data = {
            'case_time_series': cases_time_series,
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




## Uncomment the below lines and run this file to test the module

# generator = DataGenerator()

# print(generator.load_national_data('cases_time_series'))
# print(generator.load_national_data('statewise').lastupdatedtime)
# print(generator.load_national_data('statewise').state)
# print(generator.load_national_data())
# print(generator.load_state_district_data().loc["Assam", "districtData"])
# print(generator.load_states_timeseries())
# print(generator.load_states_tests_timeseries().state)