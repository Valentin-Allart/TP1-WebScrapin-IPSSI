import streamlit as st
from selenium import webdriver
from selenium.webdriver.common.by import By
import sqlalchemy as db
from database import DataBase
import time

st.set_page_config(page_title="TP1 - WebScraping", page_icon="🧊", layout="wide")
st.title("Données Doctolib")

def collect_data(selection):
    data = []
    for element in selection:
        name = element.find_element(By.TAG_NAME, "h2").text
        image = element.find_element(By.TAG_NAME, "img").get_attribute("src")
        data.append({"name": name, "image": image})
    return data

# def get_doctolib_infos(searchValue, searchCity):
#     url = f'https://www.doctolib.fr/{searchValue}/{searchCity}'
#     driver = webdriver.Chrome()
#     driver.get(url)
#     time.sleep(3)
#     driver.find_element(By.ID, "didomi-notice-agree-button").click()
#     selections = driver.find_elements(By.TAG_NAME, "article")
#     data = collect_data(selections)
#     return data

def get_doctolib_infos(searchValue, searchCity,num):
    url = f'https://www.doctolib.fr/{searchValue}/{searchCity}?page={num}'
    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(3)
    driver.find_element(By.ID, "didomi-notice-agree-button").click()
    selections = driver.find_elements(By.TAG_NAME, "article")
    data = collect_data(selections)
    return data

def save_data(data):
    database = DataBase('data')
    database.drop_rows('listeMedecin')
    for element in data:
        try:
            #check if the name is already in the database
            if len(database.check_double('listeMedecin', title=element['name'])) > 0:
                st.warning(f"Row {element['name']} already exist in the database")
            else:
                database.add_row('listeMedecin', title=element['name'], image=element['image'])
                st.success('Row successfully added to the database')
        except:
            st.error('Error while adding row to the database')

with st.form('doctolibForm'):
    searchValue = st.text_input('Quel est votre recherche ?')
    searchCity = st.text_input('Quel est votre ville ?')
    searchPage = st.slider('Combien de pages souhaitez-vous voir ?',1,5,step=1)
    if st.form_submit_button(label='Rechercher'):
        # data = get_doctolib_infos(searchValue, searchCity)
        data = []
        for i in range(1,searchPage):
            data += get_doctolib_infos(searchValue, searchCity,i)
        st.write(data)
        save_data(data)


