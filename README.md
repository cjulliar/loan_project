# loan_project

## Description du projet

Projet réalisé dans le cadre de la formation "Développeur en Intelligence Artificielle" de Simplon.

L'objectif de ce projet est de créer un modèle de machine learning (classification binaire) afin de prédire la capacité d'une entreprise à rembourser un prêt ou non, à partir d'un jeu de données historiques issu de la SBA (Small Business Administration). Le projet implique un processus rigoureux de nettoyage, d'exploration et de modélisation des données en évitant le data leaking. Le projet comporte aussi une composante de développement web et d'API, avec l'objectif de mettre le modèle en production via une interface utilisateur (framework Django) permettant de réaliser une prédiction grâce à un appel d'API (FastAPI).

## Lancer le projet en local

Le projet est décomposé en trois dossiers contenant la partie machine learning, l'API et l'application web. Un fichier requirements.txt est présent à la racine du projet permettant d'installer les dépendances nécessaires au fonctionnement des différentes parties. Il y a également des fichiers requirements distinct présent dans chaque dossier permettant d'installer uniquement les dépendances nécessaires au fonctionnement de la partie concernée.

### Partie ML

Afin de lancer les différents notebooks de la partie ml, il faut préalablement télécharger le dataset depuis ce [lien](https://drive.google.com/file/d/12oxHIUwcp-MQGsQXaEIsP8KdZVFpb0na/view), qu'il faudra placer dans un dossier datasets à la racine du dossier ml.

### Partie API

L'API peut être lancer directement en CLI avec uvicorn ou grâce à un container docker.

### Partie web app

Afin de rendre la partie web fonctionnelle il faut en premier lieu créer un fichier .env à la racine du dossier app, pour renseigner les variables d'environnement suivantes :
- SECRET_KEY=""
- DEBUG=1
- API_URL="api:8042/predict"
- POSTGRES_RDY=0
- POSTGRES_DB=
- POSTGRES_PASSWORD=
- POSTGRES_USER=
- POSTGRES_HOST=postgres_db
- POSTGRES_PORT=5432

Pour lancer la partie web app (et l'API permettant de réaliser les prédictions), l'option recommandée est d'éxécuter le docker compose à la racine du projet.