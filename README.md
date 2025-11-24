# Analyse CORD-19 — Streamlit + Notebook

Résumé
-----
Ce dépôt contient deux éléments principaux pour analyser le jeu de données CORD-19 :
- un script Streamlit interactif (`cord19.py`) pour visualiser rapidement les métadonnées ;
- un notebook Jupyter (`cord19.ipynb`) où le travail a été réalisé directement sur Kaggle (trafic/chemins adaptés à l'environnement Kaggle).

Important : dans le notebook, les données ont été chargées depuis un chemin Kaggle. Pour exécuter le notebook localement, modifiez la variable `DATA_PATH` (ou le chemin utilisé) pour pointer vers votre copie locale du fichier CSV.

Fichiers
--------
- cord19.py — application Streamlit :
  - charge `metadata_cleaned.csv` (attendre un fichier nettoyé nommé ainsi dans le même dossier ou ajuster le nom),
  - propose plusieurs visualisations (publications par année, top journaux, distribution par source, mots fréquents dans les titres),
  - affiche un aperçu du DataFrame.
- cord19.ipynb — notebook d'analyse (travail réalisé sur Kaggle) :
  - chargement et exploration initiale du dataset,
  - nettoyage et prétraitement,
  - analyses et visualisations (barplots, wordcloud),
  - sauvegarde d'un CSV nettoyé et d'une image wordcloud.

Dépendances (exemples d'installation)
------------------------------------
Python 3.8+
Pip:
pip install pandas matplotlib seaborn streamlit wordcloud

Exécution
---------
1. Streamlit  :
   streamlit run cord19.py

2. Notebook :
   - Si vous ouvriez le notebook localement, lancez Jupyter ou ouvrez le notebook dans votre IDE.
   - Sur Kaggle, le notebook a été exécuté tel quel ; pour l'exécuter localement, changez uniquement le chemin du dataset (voir section suivante).

Adaptation du notebook (note importante)
---------------------------------------
- Le notebook a été développé/exécuté sur Kaggle. Il utilise une variable `DATA_PATH` pointant vers le dataset Kaggle (ex: `/kaggle/input/CORD-19-research-challenge/metadata.csv`).
- Pour exécuter localement, modifier `DATA_PATH` pour pointer vers votre fichier local (ex: `"./metadata.csv"`).
- Vérifiez également le nom du fichier de sortie attendu par `cord19.py` : il tente de charger `metadata_cleaned.csv`. Si le notebook a sauvegardé un fichier avec un autre nom (ex: `metadata_cleanned.csv`), renommez-le ou mettez à jour le script/noms de fichiers.

Petit rapport — ce qui a été fait dans le notebook
--------------------------------------------------
1. Chargement des données
   - Lecture du CSV principal (`metadata.csv` sur Kaggle).
   - Affichage des premières lignes et info du DataFrame.

2. Exploration initiale
   - Calcul des pourcentages de valeurs manquantes par colonne.
   - Identification et suppression des colonnes contenant >40% de valeurs manquantes.

3. Nettoyage
   - Suppression des identifiants non nécessaires (ex : `cord_uid`, `s2_id`, `doi`, `url`) si présents.
   - Conversion de `publish_time` en datetime et extraction de l'année (`year`).
   - Suppression des lignes sans `year` ou `title` (nécessaires pour les graphiques).
   - Remplissage des valeurs manquantes pour `abstract`, `authors`, `journal` avec des valeurs par défaut (`'No Abstract Available'`, `'Unknown'`).
   - Sauvegarde finale d'un fichier nettoyé (vérifier le nom exact écrit par le notebook).

4. Analyses et visualisations
   - Calcul du nombre d'articles par année.
   - Identification des top journaux publishant des articles.
   - Extraction et comptage des mots fréquents dans les titres (résultat textuel).
   - Visualisations réalisées : barplots pour l'évolution par année, top journaux, distribution par source.
   - Génération et sauvegarde d'un wordcloud des titres (`wordcloud_titles.png`).

5. Résultats sauvegardés
   - Un CSV nettoyé (nom à vérifier dans le notebook).
   - Une image `wordcloud_titles.png` générée et sauvegardée.

Remarques et conseils pratiques
------------------------------
- Vérifiez les noms de fichiers (metadata.csv, metadata_cleaned.csv, metadata_cleanned.csv) et harmonisez-les.
- Pour de grandes tailles de dataset, utilisez l'option `low_memory=False` lors de la lecture et/ou échantillonnez pour tests rapides.
- Le script Streamlit utilise le cache pour le chargement (`@st.cache_data`) — utile pour itérations rapides.
- Pour reproduire exactement l'environnement Kaggle, exécutez le notebook sur Kaggle ou adaptez les chemins locaux.

Contact / Suite
---------------
Utilisez ce README comme guide pour lancer et adapter l'analyse. Pour toute adaptation supplémentaire (ex: enrichissement des visualisations, analyses textuelles avancées), mettre à jour le notebook ou le script Streamlit en conséquence.
