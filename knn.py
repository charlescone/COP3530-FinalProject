import numpy as np
import pandas as pd
import os

from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity
from fuzzywuzzy import fuzz

class Knn:
    def __init__(self):
        data_path = './data'
        movie_filename = 'movie.csv'
        ratings_filename = 'rating.csv'
        # Load the MovieLens 20M dataset (assuming ratings.csv is available)
        self.movie_df = pd.read_csv(os.path.join(data_path, movie_filename),
                                    usecols=['movieId', 'title'],
                                    dtype={'movieId': 'int32', 'title': 'str'})

        self.rating_df = pd.read_csv(os.path.join(data_path, ratings_filename),
                                     usecols=['userId', 'movieId', 'rating'],
                                     dtype={'userId': 'int32', 'movieId': 'int32', 'rating': 'float32'})

        # clean data

        df_ratings_cleaned = self.clean_data()

        self.movie_user_mat = df_ratings_cleaned.pivot(index='movieId', columns='userId', values='rating').fillna(0)
        # dict with key value pairs, key being movieId, value is movie title
        self.movie_to_index = {
            movie: i for i, movie in
            enumerate(list(self.movie_df.set_index('movieId').loc[self.movie_user_mat.index].title))
        }

        self.movie_user_mat_sparse = csr_matrix(self.movie_user_mat.values)

    # O(nlogn), groupby() is like sorting for pandas dataframes
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

    # https://www.datacamp.com/tutorial/fuzzy-string-python
    # needed fuzzy string matching to parse user input
    # to get corresponding movieID even if spelling is not exactly equal
    # O(n^3) for this function
    def fuzzy_matching(self, fav_movie):
        match_arr = []
        # get matches
        # O(n^3), fuzz.ratio is O(n^2) and we iterate over all n items
        for title, movie_id in self.movie_to_index.items():
            ratio = fuzz.ratio(title.lower(), fav_movie.lower())
            if ratio >= 60:
                match_arr.append((title, movie_id, ratio))
        # sort O(nlogn)
        match_arr = sorted(match_arr, key=lambda x: x[2])[::-1]

        return match_arr[0][1]

    # Function to get movie recommendations based on KNN
    # runs in O(n^3) + O(n*m*k) as explained below
    def get_movie_recommendations(self, movie_title, k=10):
        index = self.fuzzy_matching(movie_title)  # O(n^3)

        movie_ratings = self.movie_user_mat_sparse[index, :].toarray()
        temp = self.movie_user_mat_sparse.toarray()

        # time complexity is O(n*m*k), n is number of rows in the first matrix,
        # m, is number of rows in the second matrix, k is number of columns in both matrices
        similarities = cosine_similarity(temp, movie_ratings)
        similarities_df = pd.DataFrame(similarities, columns=['score'])
        indices = similarities_df.sort_values(by=['score'], ascending=False)  # O(nlogn) sort
        indices_list = indices.index.tolist()[1:k + 1]

        return indices_list

    # Function for checking results in console
    def print_movie_title(self, movieId):
        for i in self.movie_to_index:
            if self.movie_to_index[i] == movieId:
                return i

    # O(n), populating the output array with movie titles
    def return_recommendation(self, movie_title):
        recommendations = self.get_movie_recommendations(movie_title)
        recommendations_titles = []
        for recommendation in recommendations:
            recommendations_titles.append(self.print_movie_title(recommendation))
        return recommendations_titles
