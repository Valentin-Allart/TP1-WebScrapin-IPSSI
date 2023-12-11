import streamlit as st
import pandas as pd

st.set_page_config(page_title="TP1 - WebScraping", page_icon="🧊", layout="wide")

#Read the csv file
df = pd.read_csv('articles.csv')

st.title("TP1 - Datacards")
# st.write(df)

#Display the information of the article for each row
for index, row in df.iterrows():
    st.write(f"**{row['Title']}**")
    st.image(row['image'])
    st.write(f"**{row['Description']}**")
    st.write(f"**{row['Link']}**")
    st.write('---')