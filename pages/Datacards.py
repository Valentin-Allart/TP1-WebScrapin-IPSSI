import streamlit as st
import pandas as pd

st.set_page_config(page_title="TP1 - WebScraping", page_icon="🧊", layout="wide")

df = pd.read_csv('articles.csv')

st.title("TP1 - Datacards")

for index, row in df.iterrows():
    st.title(f"**{row['Title']}**")
    st.image(row['image'])
    st.subheader(f"**{row['Description']}**")
    st.write(f"**{row['Link']}**")
    st.write('---')