import streamlit as st

# --- CŒUR DU SYSTÈME (SpiderWorld Organique) ---
class SpiderWorld:
    @staticmethod
    def quintessence(question, ia_list, pays):
        if not ia_list: return "Sélectionnez au moins une IA."
        
        reponses = []
        for ia in ia_list:
            # Vérification sécurisée de la clé API via Secrets
            try:
                cle_api = st.secrets[f"{ia.upper()}_API_KEY"]
                reponses.append(f"[{ia}]: Analyse effectuée via clé sécurisée.")
            except:
                reponses.append(f"[{ia}]: Clé API non configurée dans les Secrets.")
            
        return f"Synthèse organique pour {pays} : \n" + "\n".join(reponses)

    @staticmethod
    def structure(pays):
        # Topologie des salons avec ancrage géographique
        return [
            {"nom": "Bio-Politique", "geo": pays, "temps": "Contemporain", "membres": 12},
            {"nom": "Environnement", "geo": "Global", "temps": "Futur", "membres": 5},
            {"nom": "Patrimoine", "geo": "Local", "temps": "Ancienne Époque", "membres": 8}
        ]

# --- INTERFACE ---
st.set_page_config(page_title="Spider-World")
st.title("Spider-World : Unité Organique")

# Paramètres du réseau humain
pays = st.selectbox("Sélectionne ton pays d'ancrage :", ["France", "Belgique", "Suisse", "Canada", "Autre"])
question = st.text_area("Ta fulgurance de sauvetage :")
ia_list = st.multiselect("IA de synergie :", ["Claude", "Gemini", "GPT-4"])

if st.button("Admission"):
    if question and ia_list:
        # Traitement via le cœur sécurisé
        synthese = SpiderWorld.quintessence(question, ia_list, pays)
        salons = SpiderWorld.structure(pays)
        
        st.write("### Quintessence", synthese)
        st.write("---")
        st.write("### Salons de résonance")
        
        for s in salons:
            col1, col2 = st.columns([3, 1])
            col1.write(f"**{s['nom']}** ({s['geo']} - {s['temps']}) | {s['membres']} membres")
            if col2.button("Rejoindre", key=s['nom']):
                st.info(f"Requête envoyée au salon {s['nom']} - Zone : {pays}.")
    else:
        st.warning("Veuillez remplir tous les champs pour l'admission.")
