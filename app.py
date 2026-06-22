import streamlit as st

# --- CŒUR DU SYSTÈME (SpiderWorld) ---
class SpiderWorld:
    @staticmethod
    def quintessence(question, ia_list):
        if not ia_list: return "Sélectionnez au moins une IA."
        return f"Synthèse organique de '{question}' par {', '.join(ia_list)}."

    @staticmethod
    def structure(question):
        # Topologie des salons
        return [
            {"nom": "Bio-Politique", "geo": "Nantes", "temps": "Contemporain", "membres": 12},
            {"nom": "Environnement", "geo": "Global", "temps": "Futur", "membres": 5},
            {"nom": "Patrimoine", "geo": "Local", "temps": "Ancienne Époque", "membres": 8}
        ]

# --- INTERFACE (Le Front) ---
st.set_page_config(page_title="Spider-World")
st.title("Spider-World : Unité Organique")

question = st.text_area("Ta fulgurance de sauvetage :")
ia_list = st.multiselect("IA de synergie :", ["Claude", "Gemini", "GPT-4"])

if st.button("Admission"):
    if question:
        # Traitement via le cœur
        synthese = SpiderWorld.quintessence(question, ia_list)
        salons = SpiderWorld.structure(question)
        
        # Affichage structuré
        st.write("### Quintessence", synthese)
        st.write("---")
        st.write("### Salons de résonance")
        
        for s in salons:
            col1, col2 = st.columns([3, 1])
            col1.write(f"**{s['nom']}** ({s['geo']} - {s['temps']}) | {s['membres']} membres")
            if col2.button("Rejoindre", key=s['nom']):
                st.info(f"Requête envoyée au salon {s['nom']}. Système de vote activé.")
    else:
        st.warning("Veuillez saisir une fulgurance.")
