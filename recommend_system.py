import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('IMDB.csv', usecols = range(0, 27))
df = df[['Title', 'Genre', 'Director', 'Actors', 'Plot']]

# Чистка данных
nltk.download('stopwords')

corpus = []
cleaning = []
key_words = []
title_list = []
Number_of_rows = df['Title'].count()
Number_of_rows += 1

for index in range(Number_of_rows):
    Genre = re.sub('[^a-zA-Z]', ' ', str(df['Genre'][index]))
    Director = re.sub(r"\s+", "", str(df['Director'][index]))
    Actors = re.sub(r"\s+", "", str(df['Actors'][index]))
    plot = re.sub('[^a-zA-Z]', ' ', str(df['Plot'][index]))
    title = re.sub('[^a-zA-Z]', ' ', str(df['Title'][index])).lower()
    title_list.append(title)
    corpus.append(Genre + ' ' + Director + ' ' + Actors + ' ' + plot)
    cleaning.append(re.sub(",", " ", corpus[index]))

for index in cleaning:
    index = index.lower()
    index = index.split()
    ps = PorterStemmer()
    index = [ps.stem(word) for word in index if not word in set(stopwords.words('english'))]
    index = ' '.join(index)
    index = str(index)
    key_words.append(index)

df['bag_of_words'] = key_words
df['Title'] = title_list

df.drop(columns=['Genre', 'Director', 'Actors', 'Plot'], inplace=True)

# Устанавливаем индекс заголовка
df.set_index(keys='Title', inplace=True)

# Создание модели
cv = CountVectorizer()
count_matrix = cv.fit_transform(df['bag_of_words']).toarray()
cosine_sim = cosine_similarity(count_matrix, count_matrix)

indices = pd.Series(df.index)

def recommender(title, cosine_sim = cosine_sim):
    recommended_movies, movies_info = [], []
    title_lower = title.lower()
    # Получаем заглавную букву фильма
    try:
        idx_title = indices[indices == title_lower].index[0]
    except IndexError:
        return "Фильма, который ты ввел нет, в базе данных. Попробуй другой"

    score_series = pd.Series(cosine_sim[idx_title]).sort_values(ascending = False)

    top_movies = list(score_series.iloc[1:4].index)

    for i in top_movies:
        recommended_movies.append(list(df.index)[i])

    return recommended_movies