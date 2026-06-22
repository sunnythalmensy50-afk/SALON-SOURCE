import streamlit as st
from salon_organique import Salon

st.title("Spider-World : Salon Organique")
st.write("Bienvenue dans l'antithèse du CAC 40. Ici, la complémentarité prime sur la quantité.")

# Interface de saisie
question = st.text_input("Quelle est ta fulgurance ?")

if st.button("Demander l'admission"):
    # Création du salon virtuel
    salon = Salon("Salon-Source")
    
    # Processus d'admission
    with st.spinner("Analyse de la complémentarité..."):
        statut = salon.processus_admission("Candidat", question)
        
    st.success(statut)
    st.write("---")
    st.write("Rappel : L'admission se base sur l'équilibre (Science, Art, Santé, Politique, IDH).")
