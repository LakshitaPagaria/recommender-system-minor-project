import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from scipy.sparse import csr_matrix

def build_user_item_matrix(ratings):
    pivot = ratings.pivot_table(index='user_id', columns='movie_id', values='rating').fillna(0)
    return pivot

def item_similarity_matrix(user_item_df):
    # user_item_df: rows = user_id, cols = movie_id
    mat = csr_matrix(user_item_df.T.values)  # shape: items x users
    sim = cosine_similarity(mat)
    sim_df = pd.DataFrame(sim, index=user_item_df.columns, columns=user_item_df.columns)
    return sim_df

def recommend_items_for_user(user_id, user_item_df, sim_df, k=10):
    user_ratings = user_item_df.loc[user_id]
    # score = similarity dot user ratings
    scores = sim_df.dot(user_ratings.fillna(0))
    # filter already rated items
    rated = user_ratings[user_ratings > 0].index
    scores = scores.drop(rated, errors='ignore')
    recs = scores.sort_values(ascending=False).head(k)
    return recs.index.tolist()
