from src.data_prep import load_movielens_100k
from src.mf_surprise import surprise_train_svd
import joblib, os

if __name__ == '__main__':
    ratings, movies, users = load_movielens_100k('data/ml-100k')
    print('Loaded:', len(ratings), 'ratings,', len(movies), 'movies,', len(users), 'users')
    algo, rmse = surprise_train_svd(ratings, n_factors=50, n_epochs=20)
    print('Trained SVD. RMSE:', rmse)
    os.makedirs('models', exist_ok=True)
    joblib.dump(algo, 'models/svd_model.pkl')
    print('Saved model to models/svd_model.pkl')
