import streamlit as st

# Configuration de la page principale
st.set_page_config(page_title="Orientation BTS SISR/SLAM", layout="wide", page_icon="🎓")

# ---------------------- FONCTIONS UTILITAIRES ---------------------- #

def afficher_message_conseil(slam_score, sisr_score):
    """Affiche un message de conseil en fonction des scores obtenus au quiz."""
    st.markdown("### Vos Résultats 📝")
    if slam_score > sisr_score:
        st.success(f"Vous êtes davantage orienté(e) vers le **SLAM (Développement)** ! 💻\n\n"
                   f"Explorez les métiers de développeur logiciel, analyste-programmeur, ou encore ingénieur en bases de données.")
    elif sisr_score > slam_score:
        st.success(f"Vous êtes davantage orienté(e) vers le **SISR (Réseau)** ! 🌐\n\n"
                   f"Découvrez des métiers comme administrateur réseau, ingénieur système ou consultant en sécurité informatique.")
    else:
        st.info(f"Vous avez un profil équilibré entre **SLAM (Développement)** et **SISR (Réseau)** ! 🖥️\n\n"
                f"Prenez le temps de découvrir les deux options pour faire un choix éclairé.")

# ---------------------- MENU DE NAVIGATION ---------------------- #
menu = st.sidebar.radio(
    "Menu de Navigation",
    [
        "Accueil",
        "Présentation des Métiers SISR",
        "Présentation des Métiers SLAM",
        "Quiz d'Orientation 🎯",
        "Jeu Éducatif : Développement vs Réseau",
        "Présentation : Lycée Simone Weil"
    ]
)

# ---------------------- PAGE ACCUEIL ---------------------- #
if menu == "Accueil":
    st.title("Bienvenue dans l'application d'orientation BTS SIO 🎓")
    st.markdown("""
        ### Objectifs de cette application :
        - **Découvrir les métiers associés** aux options SISR et SLAM.
        - **Participer à un quiz** pour identifier votre orientation idéale.
        - **Jouer à un mini-jeu éducatif** pour explorer les métiers de l'informatique.
        - Découvrir le **Lycée Simone Weil** et ses avantages pour poursuivre vos études.
    """)

# ---------------------- PAGE PRÉSENTATION SISR ---------------------- #
elif menu == "Présentation des Métiers SISR":
    st.title("SISR : Solutions d’Infrastructure, Systèmes et Réseaux 🌐")
    st.markdown("""
        ### Présentation :
        L'option **SISR** forme des spécialistes en gestion des infrastructures informatiques. 
        Ces professionnels assurent la disponibilité, la sécurité et le bon fonctionnement des réseaux et des systèmes.
        
        ### Débouchés :
        - Administrateur Réseau
        - Technicien Support Informatique
        - Consultant en Sécurité des Systèmes
        - Ingénieur Systèmes et Réseaux

        ### Salaires :
        - Débutant : entre **25 000 € et 30 000 € brut annuel**
        - Confirmé : jusqu'à **45 000 € brut annuel**
        - Expert : **60 000 € brut annuel ou plus**

        ### Missions :
        - Installer et configurer des serveurs et réseaux.
        - Assurer la sécurité informatique des infrastructures.
        - Répondre aux incidents et effectuer la maintenance.

        ### Formations Accessibles :
        - **BTS SIO**, option SISR.
        - Licences professionnelles en réseaux et télécommunications.
        - Certifications (Cisco, Microsoft, AWS, etc.).
    """)

# ---------------------- PAGE PRÉSENTATION SLAM ---------------------- #
elif menu == "Présentation des Métiers SLAM":
    st.title("SLAM : Solutions Logicielles et Applications Métiers 💻")
    st.markdown("""
        ### Présentation :
        L'option **SLAM** forme des professionnels du développement logiciel. 
        Ces experts conçoivent, développent et maintiennent des solutions informatiques adaptées aux besoins des entreprises.
        
        ### Débouchés :
        - Développeur Logiciel
        - Analyste Programmeur
        - Ingénieur en Bases de Données
        - Consultant en Développement Applicatif

        ### Salaires :
        - Débutant : entre **28 000 € et 35 000 € brut annuel**
        - Confirmé : jusqu'à **50 000 € brut annuel**
        - Expert : **70 000 € brut annuel ou plus**

        ### Missions :
        - Développer des applications web, mobiles ou logicielles.
        - Concevoir et gérer des bases de données.
        - Tester et déployer des solutions logicielles.

        ### Formations Accessibles :
        - **BTS SIO**, option SLAM.
        - Licences professionnelles en développement logiciel.
        - Certifications (Java, Python, Azure, etc.).
    """)

# ---------------------- PAGE QUIZ D'ORIENTATION ---------------------- #
elif menu == "Quiz d'Orientation 🎯":
    st.title("Quiz d'Orientation : SISR ou SLAM ?")
    st.markdown("Répondez aux questions suivantes pour découvrir votre orientation idéale.")

    questions = [
        {"question": "Préférez-vous résoudre des problèmes logiques ou créer des solutions artistiques ?", "options": ["Problèmes logiques", "Solutions artistiques"], "sisr": 1, "slam": 1},
        {"question": "Aimez-vous configurer et maintenir des réseaux informatiques ?", "options": ["Oui", "Non"], "sisr": 2, "slam": 0},
        {"question": "Êtes-vous attiré(e) par le développement d'applications mobiles ou web ?", "options": ["Oui", "Non"], "sisr": 0, "slam": 2},
        {"question": "Aimez-vous explorer les protocoles réseau et la cybersécurité ?", "options": ["Oui", "Non"], "sisr": 2, "slam": 0},
        {"question": "Préférez-vous écrire du code ou configurer du matériel ?", "options": ["Écrire du code", "Configurer du matériel"], "sisr": 0, "slam": 2},
        {"question": "Aimez-vous travailler sur des bases de données et leur structure ?", "options": ["Oui", "Non"], "sisr": 1, "slam": 1},
        {"question": "Préférez-vous travailler sur l'interface utilisateur ou sur le backend ?", "options": ["Interface utilisateur", "Backend"], "sisr": 0, "slam": 2},
    ]

    if "question_index" not in st.session_state:
        st.session_state.question_index = 0
        st.session_state.slam_score = 0
        st.session_state.sisr_score = 0

    current_question = questions[st.session_state.question_index]
    st.markdown(f"### Question {st.session_state.question_index + 1} : {current_question['question']}")
    choix = st.radio("Choisissez une option :", current_question["options"], key=f"q{st.session_state.question_index}")

    if st.button("Suivant"):
        if choix == current_question["options"][0]:
            st.session_state.sisr_score += current_question["sisr"]
            st.session_state.slam_score += current_question["slam"]
        elif choix == current_question["options"][1]:
            st.session_state.sisr_score += current_question["sisr"]
            st.session_state.slam_score += current_question["slam"]

        if st.session_state.question_index < len(questions) - 1:
            st.session_state.question_index += 1
        else:
            afficher_message_conseil(st.session_state.slam_score, st.session_state.sisr_score)
            st.button("Recommencer", on_click=lambda: st.session_state.update({"question_index": 0, "slam_score": 0, "sisr_score": 0}))

# ---------------------- JEU ÉDUCATIF ---------------------- #
elif menu == "Jeu Éducatif : Développement vs Réseau":
    st.title("Jeu Éducatif : Découvrez les Métiers de l'Informatique 🕹️")

    # Liste des questions et réponses du jeu
    questions_jeu = [
        {"question": "Que fait un administrateur réseau ?", "emoji": "🌐", "options": ["Gère les serveurs", "Code des sites web", "Répare les PC"], "reponse": "Gère les serveurs", "conseil": "Un administrateur réseau est responsable de la gestion des serveurs et des infrastructures réseau. Il veille à la sécurité et au bon fonctionnement du réseau."},
        {"question": "Quel langage est souvent utilisé en développement web ?", "emoji": "💻", "options": ["HTML/CSS", "Python", "C++"], "reponse": "HTML/CSS", "conseil": "HTML et CSS sont les langages de base pour la création de sites web. HTML structure le contenu et CSS le rend visuellement attrayant."},
        {"question": "Quel métier crée des applications mobiles ?", "emoji": "📱", "options": ["Développeur mobile", "Administrateur réseau", "Consultant en cybersécurité"], "reponse": "Développeur mobile", "conseil": "Le développeur mobile crée des applications pour smartphones et tablettes, en utilisant des technologies comme Java, Swift ou React Native."},
        {"question": "Qu'est-ce qu'un développeur backend ?", "emoji": "💾", "options": ["Travaille sur l'interface utilisateur", "Gère la logique des applications et la base de données", "Répare des équipements informatiques"], "reponse": "Gère la logique des applications et la base de données", "conseil": "Un développeur backend s'occupe de la gestion des données et de la logique de l'application côté serveur, souvent avec des langages comme Python ou Node.js."},
        {"question": "Que fait un ingénieur en cybersécurité ?", "emoji": "🔒", "options": ["Développe des applications", "Protège les systèmes et réseaux contre les attaques", "Configure des serveurs"], "reponse": "Protège les systèmes et réseaux contre les attaques", "conseil": "L'ingénieur en cybersécurité est responsable de la protection des infrastructures informatiques et des données contre les menaces externes."}
    ]

    if "jeu_index" not in st.session_state:
        st.session_state.jeu_index = 0
        st.session_state.score = 0

    # Récupère la question actuelle
    q_jeu = questions_jeu[st.session_state.jeu_index]
    st.markdown(f"{q_jeu['emoji']} **{q_jeu['question']}**")
    choix_jeu = st.radio("Vos options :", q_jeu["options"])

    # Fonction pour vérifier la réponse
    def verifier_reponse():
        if choix_jeu == q_jeu["reponse"]:
            st.session_state.score += 1
            st.success("Bonne réponse ! 🎉")
        else:
            st.error("Mauvaise réponse. Essayez encore ! 😔")
        st.info(q_jeu["conseil"])

    if st.button("Suivant ➡️"):
        verifier_reponse()
        # Passe à la question suivante
        st.session_state.jeu_index = (st.session_state.jeu_index + 1) % len(questions_jeu)

    # Affiche le score actuel
    st.markdown(f"### Score actuel : {st.session_state.score} / {len(questions_jeu)}")

    # Option pour recommencer le jeu
    if st.button("Recommencer le jeu"):
        st.session_state.jeu_index = 0
        st.session_state.score = 0


# ---------------------- PAGE PRÉSENTATION LYCÉE ---------------------- #
elif menu == "Présentation : Lycée Simone Weil":
    st.title("Lycée Simone Weil : Découvrez Notre Établissement 🏫")
    st.image("https://via.placeholder.com/300x150.png?text=Lyc%C3%A9e+Simone+Weil", caption="Lycée Simone Weil à Saint-Étienne")
    st.markdown("""
        ### Pourquoi choisir le Lycée Simone Weil ?
        - **Enseignants expérimentés** dans le domaine informatique.
        - **Infrastructure moderne** avec des salles informatiques équipés.
        - **Proximité avec les entreprises** locales pour faciliter les stages et alternances.
        - Une ambiance propice à l'apprentissage et à la réussite.
        
        ### Contact :
        - Adresse : 63 avenue Albert Raimond - BP 54 - 42272 Saint-Priest-en-Jarez
        - Téléphone : +33 0477921262
        - Email : ce.0420044V@ac-lyon.fr
        - Site : https://simone-weil.ent.auvergnerhonealpes.fr
    """)
