"# NLP" 

L’analyse de sentiments des tweets est une des applications classiques du NLP. Dans ce projet, l’idée sera de pouvoir analyser les sentiments d’un tweets à partir des mots utilisés "Coronavirus" en utilisant TextBlob. Ce qui constituera une métrique de l’angoisse globale liée au Covid-19 qui règne sur Twitter, en fonction de ce qui y est publié

Le travail consiste en l’utilisation du module Python 'Twitterscrapper'. Nous permettant d'extraire un grand nombre de tweets en spécifiant des critères de date, de langues et en nous limitant aux tweets qui contiennent certains mots-clés. 

Les Tweets, étant moins structurés, certains utilisent des emojis, l’utilisation de ponctuations est beaucoup plus présente, les fautes d’orthographes sont très courantes. Tout ceci complique le travail de nettoyage préalable.

Pour cela, nous allons passer par le module TextBlob. Ce module a une option qui permet de mesurer le sentiment d’un texte donné. En sortie la fonction nous donne un coefficient de polarité et un coefficient de sensibilité.

Dans notre cas nous avons pris en considération les Tweets contenant le mot clé "Coronavirus" datant du 16 Mars 2020 au 20 Juin 2020, et limités à 1000 Tweets extraits ! 

- Le fichier temp.py contient le code source utilisé pour cela (Utilisé l'IDE Spyder)
- Le fichier de données "tweet_covid.csv" contient les tweets extraits suivant les paramètres mis en place.
- La présentation NLP.pptx présente en général la méthode que nous avons utilisé et le but de chaque action 
- La piste vidéo NLP.mp4 présente une idée sur l'exécution du code contenu dans le fichier temp.py
