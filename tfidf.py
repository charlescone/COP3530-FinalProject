import pandas as pd
import numpy as np
from fuzzywuzzy import fuzz

from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity


class TfIdf:
    def __init__(self):
        self.movie_title_df = pd.read_csv("./data/movie.csv",
                                          usecols=['movieId', 'title'],
                                          dtype={'movieId': 'int32', 'title': 'str'})

        self.movie_df = pd.read_csv("./data/movie.csv",
                                    usecols=['movieId', 'genres'],
                                    dtype={'movieId': 'int32', 'genres': 'str'})

        # O(n) for
        # dict with key value pairs, key being movieId, value is movie title
        self.movie_to_index = {
            movie: i for i, movie in
            enumerate(list(self.movie_title_df.set_index('movieId').loc[self.movie_title_df.movieId].title))
        }

    # O(n^3) for this function
    def fuzzy_matching(self, fav_movie):
        match_arr = []
        # get matches
        # O(n^3), fuzz.ratio is O(n^2) and we iterate over all n items
        for title, movieId in self.movie_to_index.items():
            ratio = fuzz.ratio(title.lower(), str(fav_movie).lower())
            if ratio >= 60:
                match_arr.append((title, movieId, ratio))
        # sort
        # O(nlogn) for sorted()
        match_arr = sorted(match_arr, key=lambda x: x[2])[::-1]

        return match_arr[0][0]

    # O(n*m) where n is the number of rows in the dataframe and m is number of genres
    def genre_tf(self):
        temp = self.movie_df
        temp['genres'] = temp['genres'].str.replace('|', ' ')

        movie_genres = temp['genres'].str.get_dummies(' ')

        tf = movie_genres.div(movie_genres.sum(axis=1), axis=0)
        return tf

    # O(n*m) where n is number of rows and m is number of genres
    def genre_idf(self):
        # Make a temp dataframe to
        temp = self.movie_df
        temp['genres'] = temp['genres'].str.replace('|', ' ')
        movie_genres = temp['genres'].str.get_dummies(' ')

        num_movies = len(movie_genres)
        # document frequency, we just want to know if something exists, thus the astype(bool)
        df = movie_genres.astype(bool).sum(axis=0)
        idf = np.log10(num_movies / df)  # inverse document frequency
        return idf

    # O(n^2*m^2) with .mul
    # which has O(n*k) where n is number of elements in the first dataframe
    # and k is number of elements in the second dataframe
    def tf_idf(self):
        return self.genre_tf().mul(self.genre_idf(), axis=1)

    # Worst Case is O(m^2*n^2) due to the similarity calculation
    def get_movie_recommendations(self, movie_title, top_n=10):
        # O(n*m), for matrix with dimensions n x m. Also O(n*m) because of self.tf_idf()
        tfidf_csr_matrix = csr_matrix(self.tf_idf().values)
        # O(n*m), n, rows in matrix, m number of columns in matrix
        similarities = cosine_similarity(tfidf_csr_matrix)

        movie_index = self.movie_title_df.loc[self.movie_title_df['title'] == self.fuzzy_matching(movie_title)].index[0]
        similar_movies = list(enumerate(similarities[movie_index]))  # O(n) for enumerating through all elements
        similar_movies_sorted = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]  # Exclude the movie itself

        top_similar_movies = similar_movies_sorted[:top_n]
        recommendation_ids = [self.movie_df.iloc[movie[0]]['movieId'] for movie in top_similar_movies]

        # O(n)
        recommendations = []
        for rec in recommendation_ids:
            recommendations.append(self.get_movie_title(rec))

        return recommendations

    def get_movie_title(self, movieId):
        # O(1), pandas dataframe uses hashing, so there is constant look up time
        movie_title = self.movie_title_df.loc[self.movie_df['movieId'] == movieId, 'title'].values
        return movie_title[0]
