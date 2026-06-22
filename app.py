import streamlit as st
import sys
import os

# Ajout dynamique du chemin pour que le serveur trouve le moteur
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from salon_organique import Salon

# Configuration de l'interface
st.set_page_config(page_title="Spider-World : Salon Organique", layout="centered")

st.title("Spider-World : Salon Organique")
st.write("Bienvenue dans l'antithèse du CAC 40. Ici, la complémentarité prime sur la quantité.")

# Initialisation du salon
if 'salon' not in st.session_state:
    st.session_state.salon = Salon("Salon-Source")

# Interface de saisie
question = st.text_input("Quelle est ta fulgurance pour rejoindre le Salon ?")

if st.button("Demander l'admission"):
    if question:
        with st.spinner("Le groupe analyse la complémentarité de ta fulgurance..."):
            # Traitement de l'admission
            statut = st.session_state.salon.processus_admission("Candidat", question)
            
        st.success(statut)
    else:
        st.warning("Tu dois formuler une fulgurance pour espérer entrer.")

st.write("---")
st.write("Rappel : L'admission se base sur l'équilibre (Science, Art, Santé, Politique, IDH).")
