import pandas as pd
import os

def load_movielens_100k(path='data/ml-100k'):
    """
    Expects MovieLens 100k files inside path:
    - u.data (ratings)
    - u.item (movies)
    - u.user (users)
    """
    ratings_cols = ['user_id', 'movie_id', 'rating', 'timestamp']
    ratings = pd.read_csv(os.path.join(path, 'u.data'), sep='\t', names=ratings_cols, encoding='latin-1')
    movies_cols = ['movie_id', 'title', 'release_date', 'video_release_date', 'IMDb_URL',
                   'unknown','Action','Adventure','Animation',"Children's",'Comedy','Crime',
                   'Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance',
                   'Sci-Fi','Thriller','War','Western']
    movies = pd.read_csv(os.path.join(path, 'u.item'), sep='|', names=movies_cols, encoding='latin-1')
    users_cols = ['user_id','age','gender','occupation','zip_code']
    users = pd.read_csv(os.path.join(path, 'u.user'), sep='|', names=users_cols, encoding='latin-1')
    return ratings, movies, users

def train_test_split(ratings, test_size=0.2, random_state=42):
    # simple random split on rows (use Surprise for better train/test in MF)
    train = ratings.sample(frac=1-test_size, random_state=random_state)
    test = ratings.drop(train.index)
    return train, test
