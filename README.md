# Suivi Crypto 📈

Application de suivi des cours de cryptomonnaies développée en **Python** avec **Streamlit**. Elle récupère des données de marché via l'API publique **CoinGecko** et propose une visualisation interactive des prix en euros.

## Fonctionnalités actuelles

- Consultation des **10 cryptomonnaies à plus forte capitalisation** retournées par CoinGecko.
- Sélection d'une cryptomonnaie dans une liste déroulante.
- Affichage de son **prix actuel en euros** et de sa **variation sur 24 heures**.
- Visualisation de son **historique de prix sur 30 jours** sous forme de graphique.
- Affichage d'un tableau avec le nom, le symbole, le prix, la variation sur 24 heures et la capitalisation des cryptomonnaies.

> **État du projet :** le suivi et la visualisation sont implémentés dans `app.py`. La prédiction des prix, évoquée dans le document de projet, n'est **pas encore implémentée** dans le code disponible.

## Technologies

- **Python** : langage principal.
- **Streamlit** : interface web interactive.
- **Pandas** : manipulation des données.
- **Requests** : appels HTTP vers l'API CoinGecko.
- **Altair** : graphiques.
- **CoinGecko API** : données de marché des cryptomonnaies.

## Installation

### Prérequis

- Python 3 installé sur votre ordinateur.
- Une connexion Internet pour interroger CoinGecko.

### Étapes

1. Cloner le dépôt :

   ```bash
   git clone https://github.com/NGASSAp/suivi-crypto.git
   cd suivi-crypto
   ```

2. Créer et activer un environnement virtuel (recommandé) :

   **Windows (PowerShell)**

   ```powershell
   python -m venv .venv
   .venv\Scripts\Activate.ps1
   ```

   **Linux / macOS**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Installer les bibliothèques nécessaires à l'application principale :

   ```bash
   pip install streamlit pandas requests altair
   ```

4. Lancer l'application :

   ```bash
   streamlit run app.py
   ```

5. Ouvrir l'adresse locale indiquée par Streamlit dans le terminal (généralement `http://localhost:8501`).

## Structure du dépôt

```text
suivi-crypto/
├── app.py
├── app2.py
├── ANALYSE ET PREDICTION DES PRIX DE CRYPTOMONNAIES.docx
└── README.md
```

- `app.py` : application Streamlit de suivi des cryptomonnaies.
- `app2.py` : ébauche d'intégration de Reddit avec PRAW, **incomplète et non opérationnelle en l'état**.
- `ANALYSE ET PREDICTION DES PRIX DE CRYPTOMONNAIES.docx` : document lié au projet.

## Source des données

L'application utilise les points d'accès suivants de l'API CoinGecko :

- `GET /api/v3/coins/markets` : données de marché des 10 cryptomonnaies affichées.
- `GET /api/v3/coins/{id}/market_chart` : historique des prix de la cryptomonnaie choisie sur 30 jours.

Les requêtes sont effectuées en euros (`vs_currency=eur`). La disponibilité des données dépend de l'API et de ses limites d'utilisation.

## Limites et pistes d'amélioration

- Ajouter la gestion des erreurs réseau et des réponses de l'API.
- Mettre en cache les données pour éviter les requêtes répétées.
- Retirer les affichages de débogage de l'interface.
- Ajouter un fichier `requirements.txt` pour figer les dépendances.
- Finaliser ou retirer l'intégration Reddit de `app2.py`.
- Développer et évaluer un module de prédiction des prix si cet objectif est conservé.

## Avertissement

Ce projet est destiné à l'apprentissage et à l'analyse de données. Les données affichées ne constituent pas un conseil financier.
