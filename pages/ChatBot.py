import streamlit as st
from pages.OpenAI import TextProcessor

openai = TextProcessor()

st.set_page_config(page_title="TP5 - ChatBot", page_icon="🧊", layout="wide")

st.title("TP5 - ChatBot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Quel est votre requête ?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    language = "Anglais"
    commande = prompt.split(" ")[0]
    request = prompt.split(" ")[1:]
    if commande == '/translate':
        response = openai.openai_translate(request, language)
    elif commande == '/generate':
        response = openai.openai_text_generator(request)
    elif commande == '/summary':
        response = openai.openai_text_summary(request)
    elif commande == '/code':
        response = openai.openai_codex(request)
    elif commande == '/imagine':
        response = openai.openai_image(request)
    else:
        response = "Commande non reconnue"
    with st.chat_message("bot"):
        if commande == '/image':
            st.image(response)
        else:
            st.markdown(response)
    st.session_state.messages.append({"role": "user", "content": prompt})