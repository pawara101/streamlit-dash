import streamlit as st
import pandas as pd
import numpy as np

data = pd.read_csv("/home/pawarad/work/python/plotly/Data/avocado_full.csv")

st.page_link("st_1.py", label="Home", icon="🏠")
st.page_link("pages/page_1.py", label="Page 1", icon="1️⃣")
st.page_link("pages/page_2.py", label="Page 2", icon="2️⃣", disabled=True)
st.page_link("http://www.google.com", label="Google", icon="🌎")

st.title("Avacado Sales")

option = st.selectbox(
    'Year',
    (data.year.unique()))

type_region = st.selectbox(
    'Year',
    (data.region.unique()))

st.markdown("### Number of Bags sold")
year_data = data[(data["year"] == option) & (data["region"]==type_region)]
print(year_data.head())


st.bar_chart(year_data, x="Date", y=["Small Bags", "Large Bags"])

