import streamlit as st
import requests
import json

# Configuration de l'interface Streamlit
st.title("Interface Ollama Serve avec orca-mini:7b")

# Entrée utilisateur pour le prompt
prompt = st.text_input("Entrez votre question :")

if st.button("Envoyer"):
    if prompt:
        # URL de l'API Ollama Serve
        url = "http://127.0.0.1:11434/api/generate"

        # Corps de la requête
        payload = {
            "model": "orca-mini:7b",
            "prompt": prompt
        }

        # En-têtes de la requête
        headers = {
            "Content-Type": "application/json"
        }

        # Envoi de la requête POST
        response = requests.post(url, headers=headers, data=json.dumps(payload))

        # Vérification du statut de la réponse
        if response.status_code == 200:
            # Récupération de la réponse en JSON
            response_json = response.json()

            # Affichage de la réponse
            st.subheader("Réponse du modèle :")
            for item in response_json:
                st.write(item['response'])  # Affiche chaque segment de réponse

        else:
            st.error(f"Erreur: {response.status_code} - {response.text}")
    else:
        st.warning("Veuillez entrer un prompt avant de cliquer sur Envoyer.")
