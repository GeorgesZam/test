import streamlit as st
import requests
import json

st.title("Interface Ollama Serve avec orca-mini:7b")

prompt = st.text_input("Entrez votre question :")

if st.button("Envoyer"):
    if prompt:
        url = "http://127.0.0.1:11434/api/generate"
        payload = {"model": "orca-mini:7b", "prompt": prompt}
        headers = {"Content-Type": "application/json"}

        try:
            response = requests.post(url, headers=headers, data=json.dumps(payload))
            response.raise_for_status()  # Lève une erreur pour les codes de statut HTTP non 200

            st.subheader("Réponse du modèle :")
            
            # Parcourir chaque ligne de la réponse en tant que JSON
            for line in response.iter_lines():
                if line:  # Filtrer les lignes vides
                    decoded_line = json.loads(line.decode('utf-8'))
                    st.write(decoded_line['response'])

        except requests.exceptions.RequestException as e:
            st.error(f"Erreur de connexion : {e}")
        except json.JSONDecodeError as e:
            st.error(f"Erreur de décodage JSON : {e}")
    else:
        st.warning("Veuillez entrer un prompt avant de cliquer sur Envoyer.")
