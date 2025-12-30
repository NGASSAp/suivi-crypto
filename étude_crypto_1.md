###  	  **SUIVI DES DONNEES CRYPTO**



Objectifs: suivi des données de crypto via l'analyse automatique des API (CoinGecko)



Tâches:

 	- importations des bibliothèques à utiliser (streamlit pour la création de l'interface web, pandas et requests pour chercher les données sur Internet)

 	- extractions des données de l'API ainsi qu'application des filtres

 	- conversion du texte brut répondu par l'API et transformation en un tableau des lignes et colonnes

 	- récupération de ces données 

&nbsp;	- affichage des noms de colonnes et du contenue complet du tableau (facultatif à cause d'une erreur)

&nbsp;	- nettoyage (sélection des colonnes essentielles). L'API renvoie énormément d'informations inutiles, d'où l'utilité du filtrage de colonnes (ajout d'une colonne)

&nbsp;	- ajout d'un sélecteur de crypto afin de pouvoir voir des variations des autres cryptos

&nbsp;	- graphiques d'évolution de la crypto sur un mois

 	- création de l'interface ( titre de l'interface, affichage des statistiques clés du bitcoin (prix et variations), affichage dynamique (st.metric crée un composant visuel élégant: si delta est positif il s'affichera en vert avec une flèche vers le haut et s'il est négatif, la flèche sera en rouge et vers le bas. st.dataframe affiche le tableau filtré. use\_container\_width permet au tableau de prendre toute la largeur de l'écran)

