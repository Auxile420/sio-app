import streamlit as st

# Configuration de la page principale
st.set_page_config(page_title="Orientation BTS SISR/SLAM", layout="wide", page_icon="🎓")

# Menu de navigation
menu = st.sidebar.radio(
    "Menu de Navigation",
    [
        "Accueil",
        "SISR : Présentation des Métiers",
        "SLAM : Présentation des Métiers",
        "Quiz d'Orientation",
        "Jeu Éducatif : Développement vs Réseau",
        "Présentation : Lycée Simone Weil"
    ]
)

# ---------------------- PAGE ACCUEIL ---------------------- #
if menu == "Accueil":
    st.title("Bienvenue dans l'application d'orientation BTS SISR et SLAM")
    st.markdown("""
        ### Objectifs de cette application :
        - Découvrir les métiers associés aux options SISR et SLAM.
        - Participer à un quiz pour identifier votre orientation idéale.
        - Jouer à un mini-jeu éducatif pour explorer les métiers.
        - Découvrir le **Lycée Simone Weil**, établissement proposant un BTS SIO de qualité.

        Utilisez le menu de navigation à gauche pour explorer les différentes sections.
    """)

# ---------------------- PAGE PRÉSENTATION SISR ---------------------- #
elif menu == "SISR : Présentation des Métiers":
    st.title("SISR : Solutions d’Infrastructure, Systèmes et Réseaux")

    st.header("Présentation")
    st.markdown("""
        L'option **SISR** forme des spécialistes en gestion des infrastructures informatiques. 
        Les professionnels de cette filière garantissent la disponibilité, la sécurité et le bon fonctionnement des réseaux et des systèmes.
    """)

    st.subheader("🔍 Débouchés")
    st.markdown("""
        - **Administrateur Réseau**
        - **Technicien Support Informatique**
        - **Consultant en Sécurité des Systèmes**
        - **Ingénieur Systèmes et Réseaux**
    """)

    st.subheader("💰 Salaires")
    st.markdown("""
        - Débutant : entre **25 000 € et 30 000 € brut annuel**
        - Confirmé : jusqu'à **45 000 € brut annuel**
        - Expert : **60 000 € brut annuel ou plus**
    """)

    st.subheader("🎯 Missions")
    st.markdown("""
        - Installer et configurer des serveurs et réseaux.
        - Assurer la sécurité informatique des infrastructures.
        - Répondre aux incidents et effectuer la maintenance.
    """)

    st.subheader("🎓 Formations Accessibles")
    st.markdown("""
        - **BTS SIO (Services Informatiques aux Organisations)**, option SISR.
        - **Licences Professionnelles** en réseaux et télécommunications.
        - **Certifications** (Cisco, Microsoft, AWS, etc.).
    """)

# ---------------------- PAGE PRÉSENTATION SLAM ---------------------- #
elif menu == "SLAM : Présentation des Métiers":
    st.title("SLAM : Solutions Logicielles et Applications Métiers")

    st.header("Présentation")
    st.markdown("""
        L'option **SLAM** forme des professionnels du développement logiciel. 
        Les experts SLAM conçoivent, développent et maintiennent des solutions informatiques adaptées aux besoins des entreprises.
    """)

    st.subheader("🔍 Débouchés")
    st.markdown("""
        - **Développeur Logiciel**
        - **Analyste Programmeur**
        - **Ingénieur en Bases de Données**
        - **Consultant en Développement Applicatif**
    """)

    st.subheader("💰 Salaires")
    st.markdown("""
        - Débutant : entre **28 000 € et 35 000 € brut annuel**
        - Confirmé : jusqu'à **50 000 € brut annuel**
        - Expert : **70 000 € brut annuel ou plus**
    """)

    st.subheader("🎯 Missions")
    st.markdown("""
        - Développer des applications web, mobiles ou logicielles.
        - Concevoir et gérer des bases de données.
        - Tester et déployer des solutions logicielles.
    """)

    st.subheader("🎓 Formations Accessibles")
    st.markdown("""
        - **BTS SIO (Services Informatiques aux Organisations)**, option SLAM.
        - **Licences Professionnelles** en développement logiciel.
        - **Certifications** (Java, Python, Azure, etc.).
    """)

# ---------------------- PAGE QUIZ ---------------------- #
elif menu == "Quiz d'Orientation":
    st.title("Quiz : Trouvez votre Orientation")

    if "q1" not in st.session_state:
        st.session_state.q1 = None
    if "q2" not in st.session_state:
        st.session_state.q2 = None
    if "q3" not in st.session_state:
        st.session_state.q3 = None

    # Question 1
    if st.session_state.q1 is None:
        st.markdown("**Question 1** : Aimez-vous créer des jeux vidéo ?")
        st.session_state.q1 = st.radio("", ["Oui", "Non"])
        if st.button("Suivant", key="q1_next"):
            st.experimental_rerun()

    # Question 2
    elif st.session_state.q2 is None:
        st.markdown("**Question 2** : Préférez-vous travailler avec des machines ou coder des solutions logicielles ?")
        st.session_state.q2 = st.radio("", ["Travailler avec des machines", "Coder des solutions logicielles"])
        if st.button("Suivant", key="q2_next"):
            st.experimental_rerun()

    # Question 3
    elif st.session_state.q3 is None:
        st.markdown("**Question 3** : Trouvez-vous plus intéressant de résoudre des problèmes réseau ou des algorithmes complexes ?")
        st.session_state.q3 = st.radio("", ["Problèmes réseau", "Algorithmes complexes"])
        if st.button("Voir mes résultats", key="q3_next"):
            st.experimental_rerun()

    # Résultats
    else:
        st.header("Résultats")
        sisr_points = (st.session_state.q1 == "Non") + (st.session_state.q2 == "Travailler avec des machines") + (st.session_state.q3 == "Problèmes réseau")
        slam_points = 3 - sisr_points

        if sisr_points > slam_points:
            st.success("Orientation recommandée : **SISR**. Vous êtes passionné par les réseaux et la sécurité informatique.")
        elif slam_points > sisr_points:
            st.success("Orientation recommandée : **SLAM**. Vous avez un talent naturel pour le développement logiciel et les solutions numériques.")
        else:
            st.info("Vous avez des intérêts équilibrés entre SISR et SLAM. Explorez davantage les deux options pour affiner votre choix.")

        # Reprendre le test
        if st.button("Reprendre le test"):
            st.session_state.q1 = None
            st.session_state.q2 = None
            st.session_state.q3 = None
            st.experimental_rerun()

# ---------------------- PAGE JEU ÉDUCATIF ---------------------- #
elif menu == "Jeu Éducatif : Développement vs Réseau":
    st.title("Jeu Éducatif : Découvrez les Métiers")
    st.markdown("""
        Testez vos connaissances sur les métiers de **Développement** et de **Réseau**.

        **Question** : Que fait un administrateur réseau ?
        """)
    choix = st.radio("Vos options :", [
        "Configure les serveurs et les réseaux.",
        "Développe des applications web.",
        "Crée des bases de données."])

    if st.button("Valider votre réponse"):
        if choix == "Configure les serveurs et les réseaux.":
            st.success("Bravo ! C'est la bonne réponse.")
        else:
            st.error("Dommage, ce n'est pas correct. Réessayez !")

# ---------------------- PAGE PRÉSENTATION LYCÉE ---------------------- #
elif menu == "Présentation : Lycée Simone Weil":
    st.title("Lycée Simone Weil : BTS SIO")

    st.image("https://example.com/simone_weil.jpg", use_column_width=True)
    st.markdown("""
        Le **Lycée Simone Weil**, situé au cœur de la région, est reconnu pour la qualité de son enseignement en informatique. 
        Le **BTS SIO (Services Informatiques aux Organisations)** proposé par cet établissement permet aux étudiants de se spécialiser en **SISR** ou **SLAM**.
    """)

    st.subheader("📚 Atouts du Lycée")
    st.markdown("""
        - Enseignants expérimentés et pédagogues.
        - Laboratoires informatiques modernes et équipés.
        - Partenariats avec des entreprises locales pour les stages.
    """)

    st.subheader("🎓 Contact")
    st.markdown("""
        - **Adresse** : 10 Rue de l'Avenir, 75000 Paris
        - **Téléphone** : +33 1 23 45 67 89
        - **Email** : contact@simoneweil.com
    """)
