### &nbsp;	  **SUIVI DES DONNEES CRYPTO**



Objectifs: suivi des données de crypto via l'analyse automatique des API (CoinGecko)



Tâches:

&nbsp;	- importations des bibliothèques à utiliser (streamlit pour la création de l'interface web, pandas et requests pour chercher les données sur Internet)

&nbsp;	- extractions des données de l'API ainsi qu'application des filtres

&nbsp;	- conversion du texte brut répondu par l'API et transformation en un tableau des lignes et colonnes

&nbsp;	- récupération de ces données et nettoyage (sélection des colonnes essentielles). L'API renvoie énormément d'informations inutiles, d'où l'utilité du filtrage de colonnes

&nbsp;	- création de l'interface ( titre de l'interface, affichage des statistiques clés du bitcoin (prix et variations), affichage dynamique (st.metric crée un composant visuel élégant: si delta est positif il s'affichera en vert avec une flèche vers le haut et s'il est négatif, la flèche sera en rouge et vers le bas. st.dataframe affiche le tableau filtré. use\_container\_width permet au tableau de prendre toute la largeur de l'écran)

