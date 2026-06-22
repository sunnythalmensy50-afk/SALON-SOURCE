import streamlit as st
from moteur_quintessence import generer_synthese
from gouvernance_salon import lister_salons_pertinents

st.set_page_config(page_title="Spider-World")
st.title("Spider-World : Salon Organique")

question = st.text_area("Quelle est ta fulgurance aujourd'hui ?")
selection_ia = st.multiselect("Choisir les IA pour la quintessence :", ["Claude", "Gemini", "GPT-4"])

if st.button("Admission"):
    with st.spinner("Quintessenciation en cours..."):
        synthese = generer_synthese(question, selection_ia)
        st.write("### Quintessence :", synthese)
        
        st.write("---")
        st.write("### Salons de résonance :")
        salons = lister_salons_pertinents(question)
        for salon in salons:
            st.button(f"Rejoindre {salon}")
