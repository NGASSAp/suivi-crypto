import streamlit as st
import pandas as pd
import requests as req

# fonction pour interroger l'API CoinGecko

def chargement_donnees():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    parametres = {
                'vs_currency': 'eur',         # on veut les prix en euros
                'order': 'market_cap_desc',   # classer par les plus grosses capitalisations
                'per_page': 5,                # limite au top 5
                'page': 1
    }

    # envoie de la commande

    reponse = req.get (url, params = parametres)            

    # transformation de JSON reçu en tableau

    return pd.DataFrame(reponse.json())     # l'API répond avec du texte brut (JSON). Pandas le transforme immédiatement en un tableau organisé avec des lignes et des colonnes

# récupération des données brutes

df_brut = chargement_donnees()

# sélection des colonnes essentielles

df_propre = df_brut [['name', 'symbol', 'current_price', 'price_change_percentage_24h', 'market_cap']]

# création de l'interface (transformation du tableau en page web interactive)

st.title ("moniteur")

# affichage d'une statistique clé

prix_btc = df_propre.iloc[0]['current_price']
variation_btc = df_propre.iloc[0]['price_change_percentage_24h']
st.metric(label = "Bitcoin", value = f"{prix_btc} € ", delta = f"{variation_btc:.2f}%")

# affichage du tableau complet des 5 premières cryptos

st.dataframe(df_propre, use_container_width=True)