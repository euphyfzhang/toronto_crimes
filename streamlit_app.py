import streamlit
import snowflake.connector
import pandas

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchall()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

my_cur.execute("SELECT * FROM ACCESS_CHECK;")
second_table = my_cur.fetchall()
streamlit.dataframe(second_table)
