from surprise import Dataset, Reader, SVD, accuracy
from surprise.model_selection import train_test_split
import pandas as pd

def surprise_train_svd(ratings_df, n_factors=50, n_epochs=20, random_state=42):
    """
    Train an SVD model using the Surprise library.
    Returns: trained algo, rmse on testset
    """
    reader = Reader(rating_scale=(1,5))
    data = Dataset.load_from_df(ratings_df[['user_id','movie_id','rating']], reader)
    trainset, testset = train_test_split(data, test_size=0.2, random_state=random_state)
    algo = SVD(n_factors=n_factors, n_epochs=n_epochs, random_state=random_state)
    algo.fit(trainset)
    preds = algo.test(testset)
    rmse = accuracy.rmse(preds, verbose=False)
    return algo, rmse

def svd_recommend(algo, user_id, movies_df, n=10):
    """
    Score all movies for a user (that exist in movies_df) and return top-n movie_ids.
    Warning: for large datasets scoring every movie can be slow.
    """
    movies = movies_df['movie_id'].unique()
    preds = []
    for mid in movies:
        try:
            est = algo.predict(user_id, mid).est
            preds.append((mid, est))
        except Exception:
            continue
    preds.sort(key=lambda x: x[1], reverse=True)
    top_n = [m for m,_ in preds[:n]]
    return top_n
