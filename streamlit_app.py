import streamlit
import snowflake.connector
import pandas
import requests

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchall()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("SELECT * FROM ACCESS_CHECK;")
second_table = my_cur.fetchall()
streamlit.dataframe(second_table)

streamlit.header('Toronto Crimes - Major Crimes Indicator')

mci_response = requests.get("https://services.arcgis.com/S9th0jAJ7bqgIRjw/arcgis/rest/services/Major_Crime_Indicators_Open_Data/FeatureServer/0/query?outFields=*&where=1%3D1&f=geojson")
mci_json = pandas.json_normalize(mci_response.json())
streamlit.dataframe(mci_json['features'])
