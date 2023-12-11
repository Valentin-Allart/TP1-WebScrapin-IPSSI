import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup

st.set_page_config(page_title="TP1 - WebScraping", page_icon="🧊", layout="wide")


st.title("TP1 - WebScraping")

def get_articles(searchPage, searchValue):
    url = f'https://www.blogdumoderateur.com/page/{searchPage}/?s={searchValue}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('article')
    articles_list = []
    for article in articles:
        title = article.find('h3').text
        link = article.find('a')['href']
        theme = article.find('span').text
        articles_list.append([title, link, theme])
    df = pd.DataFrame(articles_list, columns=['Title', 'Link', 'Description'])
    df.to_csv('articles.csv', index=False)
    st.dataframe(df)


with st.form('Form'):
    searchValue = st.text_input('Quel est votre recherche ?')
    searchPage = st.number_input('Quel est le numéro de la page ?',1,25,step=1)
    if st.form_submit_button(label='Rechercher'):
        get_articles(searchPage, searchValue)