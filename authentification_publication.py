# streamlit run authentification_publication.py

import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

lesDonneesDesComptes = {
    "usernames": {
        "utilisateur": {
            "name": "utilisateur",
            "password": "utilisateurMDP",
            "email": "utilisateur@gmail.com",
            "failed_login_attemps": 0,  # Sera géré automatiquement
            "logged_in": False,  # Sera géré automatiquement
            "role": "utilisateur",
        },
        "root": {
            "name": "root",
            "password": "rootMDP",
            "email": "admin@gmail.com",
            "failed_login_attemps": 0,  # Sera géré automatiquement
            "logged_in": False,  # Sera géré automatiquement
            "role": "administrateur",
        },
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",  # Le nom du cookie, un str quelconque
    "cookie key",  # La clé du cookie, un str quelconque
    30,  # Le nombre de jours avant que le cookie expire
)

authenticator.login()

nom = st.session_state.get("username")

with st.sidebar:

    def accueil():

        username = st.session_state.get("username")

    if st.session_state["authentication_status"]:
        accueil()
        # Le bouton de déconnexion
        authenticator.logout("Déconnexion")

    elif st.session_state["authentication_status"] is False:
        st.error("L'username ou le password est/sont incorrect")
    elif st.session_state["authentication_status"] is None:
        st.warning("Les champs username et mot de passe doivent être remplie")

    st.text(f"Bienvenue {nom}")

    selection = option_menu(
        menu_title=None, options=[" 😍 Accueil", " 📷 Photos New-York"]
    )

# --------------------- Page centrale ----------------------#

if selection == " 😍 Accueil":
    st.title("Bienvenue sur ma page")
    st.image(
        "https://media.istockphoto.com/id/624265498/fr/photo/pont-de-manhattan-new-york.jpg?s=2048x2048&w=is&k=20&c=990YYbbwHJaAGzC4j1chWw9hPfreCB8o4eeK3YeQwuI="
    )

elif selection == " 📷 Photos New-York":
    st.header("🚖 Album New-York 🗽​")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image(
            "https://as1.ftcdn.net/v2/jpg/01/09/94/26/1000_F_109942636_reFxJ0J63CHUYRmlOAKsIixxiWEZX4oE.jpg"
        )
    with col2:
        st.image(
            "https://www.okvoyage.com/wp-content/uploads/2023/11/new-york-en-photos-1536x1025.jpg",
            width=500,
        )
    with col3:
        st.image(
            "https://milesandlove.com/system/attachments/2555/xxlarge/new-york-et-yellow-cab-la-nuit.jpg?1509451499"
        )
