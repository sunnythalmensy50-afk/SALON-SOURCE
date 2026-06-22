import streamlit as st
import openai
import anthropic
import google.generativeai as genai

# --- CŒUR DU SYSTÈME (SpiderWorld Organique) ---
class SpiderWorld:
    @staticmethod
    def get_ai_response(ia, question):
        """Récupère la réflexion réelle de l'IA sélectionnée."""
        try:
            if ia == "GPT-4":
                client = openai.OpenAI(api_key=st.secrets["GPT-4_API_KEY"])
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[{"role": "user", "content": question}]
                )
                return response.choices[0].message.content
            
            elif ia == "Claude":
                client = anthropic.Anthropic(api_key=st.secrets["CLAUDE_API_KEY"])
                response = client.messages.create(
                    model="claude-3-opus-20240229",
                    max_tokens=1000,
                    messages=[{"role": "user", "content": question}]
                )
                return response.content[0].text
            
            elif ia == "Gemini":
                genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
                model = genai.GenerativeModel('gemini-pro')
                response = model.generate_content(question)
                return response.text
            
            return "Modèle non supporté."
        except Exception as e:
            return f"Erreur de réflexion [{ia}] : {str(e)}"

    @staticmethod
    def quintessence(question, ia_list, pays):
        if not ia_list: return "Sélectionnez au moins une IA."
        
        results = {}
        for ia in ia_list:
            # Appel de la réflexion réelle
            results[ia] = SpiderWorld.get_ai_response(ia, question)
            
        return results

    @staticmethod
    def structure(pays):
        return [
            {"nom": "Bio-Politique", "geo": pays, "temps": "Contemporain", "membres": 12},
            {"nom": "Environnement", "geo": "Global", "temps": "Futur", "membres": 5},
            {"nom": "Patrimoine", "geo": "Local", "temps": "Ancienne Époque", "membres": 8}
        ]

# --- INTERFACE ---
st.set_page_config(page_title="Spider-World", layout="wide")
st.title("Spider-World : Unité Organique")

pays = st.selectbox("Sélectionne ton pays d'ancrage :", ["France", "Belgique", "Suisse", "Canada", "Autre"])
question = st.text_area("Ta fulgurance de sauvetage :")
ia_list = st.multiselect("IA de synergie :", ["Claude", "Gemini", "GPT-4"])

if st.button("Admission"):
    if question and ia_list:
        with st.spinner("Le système déploie ses synapses..."):
            synthese_data = SpiderWorld.quintessence(question, ia_list, pays)
            salons = SpiderWorld.structure(pays)
        
        st.write("### Quintessence (Réflexions)")
        for ia, reponse in synthese_data.items():
            with st.expander(f"Réflexion de {ia}"):
                st.write(reponse)
        
        st.write("---")
        st.write("### Salons de résonance")
        for s in salons:
            col1, col2 = st.columns([3, 1])
            col1.write(f"**{s['nom']}** ({s['geo']} - {s['temps']}) | {s['membres']} membres")
            if col2.button("Rejoindre", key=s['nom']):
                st.info(f"Requête envoyée au salon {s['nom']} - Zone : {pays}.")
    else:
        st.warning("Veuillez remplir tous les champs pour l'admission.")
