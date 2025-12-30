import streamlit as st
import pandas as pd
import requests as req
import altair as alt

# fonction pour interroger l'API CoinGecko

def chargement_donnees():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    parametres = {
                'vs_currency': 'eur',         # on veut les prix en euros
                'order': 'market_cap_desc',   # classer par les plus grosses capitalisations
                'per_page': 10,                # limite au top 5
                'page': 1
    }

    # envoie de la commande

    reponse = req.get (url, params = parametres)            

    # transformation de JSON reçu en tableau

    return pd.DataFrame(reponse.json())     # l'API répond avec du texte brut (JSON). Pandas le transforme immédiatement en un tableau organisé avec des lignes et des colonnes

# récupération des données brutes

df_brut = chargement_donnees()
st.write(df_brut.columns) # afficher les noms des colonnes
st.dataframe(df_brut) # voir le contenu complet du tableau

# sélection des colonnes essentielles

df_propre = df_brut [['id', 'name', 'symbol', 'current_price', 'price_change_percentage_24h', 'market_cap']]

# création de l'interface (transformation du tableau en page web interactive)

st.title ("moniteur")

# sélecteur de crypto

crypto_choix = st.selectbox ("choisis une crypto", df_propre['name'])    # st.selectbox affiche une liste déroutante dans la page, le texte affiché au dessus c'est choisis..., df_propre['name'] est la liste des noms des cryptos

ligne = df_propre[df_propre['name'] == crypto_choix].iloc[0]    # df_propre['name'] == crypto_choix filtre le tableau pour ne garder que la ligne où le nom correspond au choix, df_propre[..] retourne le tablau filtré, .iloc[0] prend la première ligne du résultat

# affichage d'une statistique clé

prix_btc = df_propre.iloc[0]['current_price']   # on prend la première ligne et on recupère current_price
variation_btc = df_propre.iloc[0]['price_change_percentage_24h']    # on prend la première ligne et on recupère price_change_percentage_24h
st.metric(label = crypto_choix, value = f"{ligne['current_price']} € ", delta = f"{ligne['price_change_percentage_24h']:.2f}%") # le fonction st.metric(..) affiche un petit widget visuel: titre, valeur et variation

# graphique d'évolution sur 7 jours

historique = req.get(f"https://api.coingecko.com/api/v3/coins/{ligne['id']}/market_chart", params={"vs_currency": "eur", "days": 30}).json()

df_histo = pd.DataFrame(historique['prices'], columns=['timestamp', 'price'])   # transformation de historique en dataframe (tableau pandas) avec deux colonnes: timestamp et price
df_histo['timestamp'] = pd.to_datetime(df_histo['timestamp'], unit='ms')     # timestamp est en millisecondes, on les convertis en dates lisibles

chart = alt.Chart(df_histo).mark_line().encode(x='timestamp:T', y = 'price:Q')    # alt.Chart(df_histo) demande à Altair d'utiliser le tableau df_histo, mark_line() pour avoir un graphique en ligne, encode(...) pour définir les axes

st.altair_chart(chart, use_container_width=True)    # affichage

# affichage du tableau complet des 10 premières cryptos

st.dataframe(df_propre, use_container_width=True)