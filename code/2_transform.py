import pandas as pd
import streamlit as st
import pandaslib as pl

# TODO: Write your transformation code here
state_data = pd.read_csv('cache/states.csv')
survey_data = pd.read_csv('cache/survey.csv')


years = survey_data['year'].unique()

col1 = pd.read_csv('cache/col_2021.csv')
col2 = pd.read_csv('cache/col_2022.csv')
col3 = pd.read_csv('cache/col_2023.csv')
col4 = pd.read_csv('cache/col_2024.csv')

cols_data = pd.concat([col1, col2, col3, col4])

survey_data['_country'] = survey_data['What country do you work in?'].apply(pl.clean_country_usa)

survey_states_combined = pd.merge(survey_data, state_data, left_on='If you\'re in the U.S., what state do you work in?', right_on='State', how='inner')

survey_states_combined['_full_city'] = survey_states_combined['What city do you work in?'] + ', ' + survey_states_combined['Abbreviation'] + ', ' + survey_states_combined['_country']

combined_data = pd.merge(survey_states_combined, cols_data, left_on=['year', '_full_city'], right_on=['year', 'City'], how='inner')

combined_data['__annual_salary_cleaned'] = combined_data['What is your annual salary? (You\'ll indicate the currency in a later question. If you are part-time or hourly, please enter an annualized equivalent -- what you would earn if you worked the job 40 hours a week, 52 weeks a year.)'].apply(pl.clean_currency)

combined_data['_annual_salary_adjusted'] = (combined_data['__annual_salary_cleaned'] / combined_data['Cost of Living Index']) * 100

combined_data.to_csv('cache/survey_dataset.csv', index=False)

pivot = combined_data.pivot_table(index='_full_city', columns='How old are you?', values='_annual_salary_adjusted', aggfunc='mean')

pivot.to_csv('cache/annual_salary_adjusted_by_location_and_age.csv')

pivot2 = combined_data.pivot_table(index='_full_city', columns='What is your highest level of education completed?', values='_annual_salary_adjusted', aggfunc='mean')

pivot2.to_csv('cache/annual_salary_adjusted_by_location_and_education.csv')