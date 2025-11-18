import streamlit as st
import pandas as pd
import plotly.express as px
import mysql.connector

# Cached function to fetch data from MySQL
@st.cache_resource
def get_data():
    conn = mysql.connector.connect(
        host=st.secrets["connections"]["mysql"]["host"],
        port=st.secrets["connections"]["mysql"]["port"],
        user=st.secrets["connections"]["mysql"]["username"],
        password=st.secrets["connections"]["mysql"]["password"],
        database=st.secrets["connections"]["mysql"]["database"]
    )
    df = pd.read_sql("SELECT * FROM dummy_data", conn)
    conn.close()
    return df

# Streamlit app
st.title("Plot data from MySQL")
st.write("Some made-up data")
df = get_data()

fig = px.scatter(df, x="date", y="value")
st.plotly_chart(fig, use_container_width=True)
