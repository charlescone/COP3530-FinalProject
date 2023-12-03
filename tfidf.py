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

        self.rating_df = pd.read_csv("./data/rating.csv",
                                     usecols=['userId', 'movieId', 'rating'],
                                     dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})
        df_ratings_cleaned = self.clean_data()
        self.movie_user_mat = df_ratings_cleaned.pivot(index='movieId', columns='userId', values='rating').fillna(0)
        # dict with key value pairs, key being movieId, value is movie title
        print()
        self.movie_to_index = {
            movie: i for i, movie in
            enumerate(list(self.movie_title_df.set_index('movieId').loc[self.movie_user_mat.index].title))
        }
        self.tfidf_csr_matrix = csr_matrix(self.tf_idf().values)

        self.similarities = cosine_similarity(self.tfidf_csr_matrix)

    def clean_data(self, popularity_threshold=40, ratings_threshold=40):
        df_movies_cnt = (
            self.rating_df.groupby('movieId')
            .size()
            .reset_index(name='count')
        )

        popular_movies = (
            df_movies_cnt[df_movies_cnt['count'] >= popularity_threshold]['movieId']
            .tolist()
        )

        df_ratings_drop_movies = (
            self.rating_df[self.rating_df['movieId'].isin(popular_movies)]
        )

        df_users_cnt = (
            df_ratings_drop_movies.groupby('userId')
            .size()
            .reset_index(name='count')
        )

        active_users = (
            df_users_cnt[df_users_cnt['count'] >= ratings_threshold]['userId']
            .tolist()
        )

        df_ratings_drop_users = (
            df_ratings_drop_movies[df_ratings_drop_movies['userId'].isin(active_users)]
        )

        return df_ratings_drop_users

    def fuzzy_matching(self, fav_movie, verbose=True):
        print(fav_movie)
        match_arr = []
        # get matches
        for title, movieId in self.movie_to_index.items():
            ratio = fuzz.ratio(title.lower(), str(fav_movie).lower())
            if ratio >= 60:
                match_arr.append((title, movieId, ratio))
        # sort
        match_arr = sorted(match_arr, key=lambda x: x[2])[::-1]
        if verbose:
            print('Found possible matches in our database: {0}\n'.format([x[0] for x in match_arr]))
        return match_arr[0][0]

    def genre_tf(self):
        temp = self.movie_df
        temp['genres'] = temp['genres'].str.replace('|', ' ')

        movie_genres = temp['genres'].str.get_dummies(' ')

        tf = movie_genres.div(movie_genres.sum(axis=1), axis=0)
        return tf

    def genre_idf(self):
        temp = self.movie_df
        temp['genres'] = temp['genres'].str.replace('|', ' ')

        movie_genres = temp['genres'].str.get_dummies(' ')
        N = len(movie_genres)
        df = movie_genres.astype(bool).sum(axis=0)
        idf = np.log10(N / df)
        return idf

    def tf_idf(self):
        return self.genre_tf().mul(self.genre_idf(), axis=1)

    def get_movie_recommendations(self, movie_title, top_n=5):
        print(self.movie_title_df[self.movie_title_df['title'] == self.fuzzy_matching(movie_title)])
        movie_index = self.movie_title_df.loc[self.movie_title_df['title'] == self.fuzzy_matching(movie_title)].index[0]
        similar_movies = list(enumerate(self.similarities[movie_index]))
        similar_movies_sorted = sorted(similar_movies, key=lambda x: x[1], reverse=True)[1:]  # Exclude the movie itself

        top_similar_movies = similar_movies_sorted[:top_n]
        recommendations = [self.movie_df.iloc[movie[0]]['movieId'] for movie in top_similar_movies]

        return recommendations

    def get_movie_title(self, movieId):
        movie_title = self.movie_title_df.loc[self.movie_df['movieId'] == movieId, 'title'].values
        return movie_title[0]
