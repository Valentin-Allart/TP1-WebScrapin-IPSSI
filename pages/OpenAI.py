import openai
import streamlit as st
# from IPython.display import Image

class TextProcessor:
    openai.api_key="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"
    def openai_translate(self, text, language):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Traduis ca en {language}:\n\n{text}\n\n",
            temperature=0.3,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        ) 
        return response.choices[0].text
    
    def openai_text_summary(self, text):
        response = openai.Completion.create(
            model="davinci",
            prompt=f"Summarize: {text}\n\n",
            temperature=0.3,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        ) 
        return response.choices[0].text
    
    def openai_text_generator(self, text):
        response = openai.Completion.create(
            model="davinci",
            prompt=f"{text}\n\n",
            temperature=1,
            max_tokens=100,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        ) 
        return response.choices[0].text
    
    def openai_codex(self, text):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "user",
                "content": f"{text}"
                }
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
            )

        return response.choices[0].text
    
    def openai_image(self,text):
        response = openai.Image.create(
        prompt=f"{text}",
        n=1,
        size="512x512"
        )
        return response['data'][0]['url']
    
    def openai_jsonify_from_url(self, url):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                "role": "system",
                "content": f"JSONIFY {url}", 
                "role": "user",
                "content": f"{text}"
                }
            ],
            temperature=1
        )
        return response.choices[0]['message']['content']
    
generate = TextProcessor()

st.set_page_config(page_title="TP5 - OpenAI", page_icon="🧊", layout="wide")

st.title("TP5 - OpenAI")

col1,col2 = st.columns(2)

with col1:
    st.header("Traduction")
    with st.form('translation'):
        text = st.text_input("Entrez votre texte")
        language = st.selectbox("Choisissez la langue",["Francais","Anglais","Espagnol","Allemand"])
        if st.form_submit_button(label='Traduire'):
            st.write(generate.openai_translate(text, language))
    st.header("Générateur de texte")
    with st.form('generator'):
        text = st.text_input("Entrez votre texte")
        if st.form_submit_button(label='Générer la suite'):
            st.write(generate.openai_text_generator(text))

with col2:
    st.header("Résumé")
    with st.form('Resumer'):
        text = st.text_input("Entrez votre texte")
        if st.form_submit_button(label='Résumer'):
            st.write(generate.openai_text_summary(text))
    st.header("Verificateur de code - En cours de dev")
    with st.form('Code'):
        text = st.text_input("Entrez votre code")
        if st.form_submit_button(label='Vérifier'):
            st.write(generate.openai_codex(text))

st.header("Image")
with st.form('Image'):
    text = st.text_input("Entrez votre texte")
    if st.form_submit_button(label='Générer l\'image'):
        st.image(generate.openai_image(text))

st.header("JSON")
with st.form('JSON'):
    text = st.text_input("Entrez votre texte")
    if st.form_submit_button(label='Générer le JSON'):
        st.write(generate.openai_jsonify_from_url(text))