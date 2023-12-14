import streamlit as st
import pandas as pd

st.set_page_config(page_title="TP1 - WebScraping", page_icon="🧊", layout="wide")

st.title("IFrame - API")

#Faire une iframe avec cette url : http://localhost:8001/docs dans un markdown
st.markdown('''
<iframe src="http://localhost:8001/docs" width="100%" height="900px" style="border: none;">
</iframe>
''', unsafe_allow_html=True)