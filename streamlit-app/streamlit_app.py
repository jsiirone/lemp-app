import streamlit as st
import mysql.connector
import pandas as pd
conn = mysql.connector.connect(
        host=st.secrets["connections"]["mysql"]["host"],
        port=st.secrets["connections"]["mysql"]["port"],
        user=st.secrets["connections"]["mysql"]["username"],
        password=st.secrets["connections"]["mysql"]["password"],
        database=st.secrets["connections"]["mysql"]["database"]
)
df = pd.read_sql('SELECT * FROM weather_data ORDER BY timestamp DESC LIMIT 50', conn)
conn.close()
st.title('Säädata Helsingistä')
st.dataframe(df)