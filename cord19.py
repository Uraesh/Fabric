import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
import re


# Load the metadata file
@st.cache_data  # Cache the data loading for performance
def load_data():
    df = pd.read_csv('metadata_cleaned.csv', low_memory=False)
    # Basic cleaning as in previous code
    df_cleaned = df.dropna(subset=['title', 'publish_time', 'journal'])
    df_cleaned['publish_time'] = pd.to_datetime(df_cleaned['publish_time'], errors='coerce')
    df_cleaned['year'] = df_cleaned['publish_time'].dt.year
    return df_cleaned


df_cleaned = load_data()

# App Title and Description
st.title("Analyse des Recherches sur la COVID-19")
st.write("""
Cette application Streamlit simple permet d'explorer le dataset CORD-19.
Elle affiche des visualisations interactives basées sur les métadonnées des articles scientifiques.
""")

# Interactive Widgets
st.sidebar.header("Options Interactives")
viz_option = st.sidebar.selectbox(
    "Choisissez une visualisation",
    ["Évolution des publications par année", "Principales revues", "Distribution par source",
     "Mots fréquents dans les titres"]
)

top_n = st.sidebar.slider("Nombre d'éléments top (pour revues/sources/mots)", min_value=5, max_value=20, value=10)

# Display Selected Visualization
if viz_option == "Évolution des publications par année":
    articles_per_year = df_cleaned['year'].value_counts().sort_index()
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(articles_per_year.index, articles_per_year.values)
    ax.set_title("Évolution du nombre de publications au fil du temps")
    ax.set_xlabel("Année")
    ax.set_ylabel("Nombre d'articles")
    plt.xticks(rotation=45)
    plt.grid(True)
    st.pyplot(fig)

elif viz_option == "Principales revues":
    top_journals = df_cleaned['journal'].value_counts().head(top_n)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(top_journals.index, top_journals.values)
    ax.set_title(f"Top {top_n} revues principales")
    ax.set_xlabel("Revues")
    ax.set_ylabel("Nombre d'articles")
    plt.xticks(rotation=90)
    plt.grid(True)
    st.pyplot(fig)

elif viz_option == "Distribution par source":
    sources = df_cleaned['source_x'].value_counts().head(top_n)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(sources.index, sources.values)
    ax.set_title(f"Distribution du nombre de papiers par source (Top {top_n})")
    ax.set_xlabel("Sources")
    ax.set_ylabel("Nombre d'articles")
    plt.xticks(rotation=90)
    plt.grid(True)
    st.pyplot(fig)

elif viz_option == "Mots fréquents dans les titres":
    titles = df_cleaned['title'].dropna().str.lower()
    all_words = []
    for title in titles:
        words = re.findall(r'\b\w+\b', title)
        all_words.extend(words)
    word_counts = Counter(all_words)
    most_common = word_counts.most_common(top_n)
    words, counts = zip(*most_common)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.bar(words, counts)
    ax.set_title(f"Top {top_n} mots les plus fréquents dans les titres")
    ax.set_xlabel("Mots")
    ax.set_ylabel("Fréquence")
    plt.xticks(rotation=90)
    plt.grid(True)
    st.pyplot(fig)

# Display Data Example
st.header("Exemple des Données")
st.write("Voici un aperçu des premières lignes du dataset :")
st.dataframe(df_cleaned.head())