# streamlit run authentification_publication.py

import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# ------------------ Données des utilisateurs ------------------ #
lesDonneesDesComptes = {
    "usernames": {
        "utilisateur": {
            "name": "utilisateur",
            "password": "utilisateurMDP",
            "email": "utilisateur@gmail.com",
            "failed_login_attempts": 0,
            "logged_in": False,
            "role": "utilisateur",
        },
        "root": {
            "name": "root",
            "password": "rootMDP",
            "email": "admin@gmail.com",
            "failed_login_attempts": 0,
            "logged_in": False,
            "role": "administrateur",
        },
    }
}

# ------------------ Authentification ------------------ #
authenticator = Authenticate(
    credentials=lesDonneesDesComptes,
    cookie_name="mon_cookie",
    key="ma_cle_cookie",
    cookie_expiry_days=30,
)

authenticator.login()

# Récupération de l'utilisateur connecté
nom_utilisateur = st.session_state.get("username")
statut_auth = st.session_state.get("authentication_status", None)


# ------------------ Définition de la page d'accueil ------------------ #
def accueil():
    st.title("Bienvenue sur l'application 📸")
    st.write("Utilisez le menu latéral pour naviguer entre les sections.")


# ------------------ Interface après connexion ------------------ #
if statut_auth:
    with st.sidebar:
        st.text(f"Bienvenue {nom_utilisateur}")
        authenticator.logout("🔒 Déconnexion", "sidebar")

        selection = option_menu(
            menu_title=None,
            options=["😍 Accueil", "📷 Photos New-York"],
            icons=["house", "camera"],
            menu_icon="cast",
            default_index=0,
        )

    if selection == "😍 Accueil":
        accueil()
        st.image(
            "https://media.istockphoto.com/id/624265498/fr/photo/pont-de-manhattan-new-york.jpg?s=2048x2048&w=is&k=20&c=990YYbbwHJaAGzC4j1chWw9hPfreCB8o4eeK3YeQwuI=",
            caption="Pont de Manhattan - New York",
        )

    elif selection == "📷 Photos New-York":
        st.header("🚖 Album New-York 🗽")
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

elif statut_auth is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect.")

elif statut_auth is None:
    st.warning("Veuillez renseigner votre nom d'utilisateur et mot de passe.")
