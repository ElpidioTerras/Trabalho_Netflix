# -*- coding: utf-8 -*-
"""Netflix

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/19Lek7LDqCjhB9f0Vqg0s2tuqHDbsyDEK

Elpidio Rezende Terras 9°Periodo


Cristiano Lima Machado 9°Periodo
"""

import pandas as pd
from collections import Counter

# URL do arquivo CSV no GitHub
url = 'https://raw.githubusercontent.com/ElpidioTerras/Trabalho_Netflix/main/netflix_titles.csv'

df = pd.read_csv(url)

#print(df.head())
#print("\nColunas do DataFrame:")
#print(df.columns)

# Imprimindo a coluna tittle e rating
#print(df[['title', 'rating']].head())

# TOp 10 series mais avaliadas
df_sorted_by_rating = df.sort_values(by='rating', ascending=False)

top_10_ratings = df_sorted_by_rating.head(10)

#print(top_10_ratings[['title', 'rating']])

#10 gêneros mais procurados
#print("\nColunas do DataFrame:")
#print(df.columns)


all_genres = df['listed_in'].str.split(',').explode().str.strip()
genre_counts = Counter(all_genres)


genre_counts_df = pd.DataFrame(genre_counts.items(), columns=['Genre', 'Count']).sort_values(by='Count', ascending=False)

#impreme nome e quantidade dos gêneros mais vistos
#print("\nGêneros mais procurados:")
#print(genre_counts_df.head(10))

#gera o grafico
plt.figure(figsize=(12, 6))
plt.barh(genre_counts_df['Genre'].head(10), genre_counts_df['Count'].head(10), color='skyblue')
plt.xlabel('Count')
plt.title('Top 10 Gêneros Mais Procurados')
plt.gca().invert_yaxis()
plt.show()

# Antigos (lançados antes de 2000)

old_movies = df[df['release_year'] < 2000]
old_movie_counts_by_year = old_movies.groupby('release_year').size()


plt.figure(figsize=(12, 6))
old_movie_counts_by_year.plot(kind='bar', color='skyblue')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Número de Filmes')
plt.title('Filmes Antigos por Ano de Lançamento')
plt.xticks(rotation=45, ha='right')
plt.show()

# Filme lançado em 1925
movie_1925 = df[df['release_year'] == 1925]
#print(movie_1925)

# Filmes lançados apartir de 2010
recent_movies = df[df['release_year'] > 2010]
recent_movie_counts_by_year = recent_movies.groupby('release_year').size()


plt.figure(figsize=(12, 6))
recent_movie_counts_by_year.plot(kind='bar', color='skyblue')
plt.xlabel('Ano de Lançamento')
plt.ylabel('Número de Filmes')
plt.title('Filmes Recentes por Ano de Lançamento')
plt.xticks(rotation=45, ha='right')
plt.show()
