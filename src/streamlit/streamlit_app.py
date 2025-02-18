import streamlit as st
from snowflake.snowpark import Session
import requests
import pandas

### Set page layout
st.set_page_config(layout="wide")

### Connection to Snowflake
session = Session.builder.configs(st.secrets["connections"]["snowflake"]).create()

test_connect = session.sql("SELECT CURRENT_ROLE();").collect()
st.dataframe(test_connect)

st.header('Toronto Crimes - Major Crimes Indicator ')

mci_response = requests.get("https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Major_Crime_Indicators_Open_Data/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson")
mci_json = pandas.json_normalize(mci_response.json())
mci_feature_json = pandas.json_normalize(mci_json['features'][0])
st.dataframe(mci_feature_json)