import pandas as pd
import random
from collections import defaultdict

from src.data_prep import load_movielens_100k
from src.mf_surprise import surprise_train_svd, svd_recommend
from src.eval_metrics import precision_at_k

# ----------------------------------------------------------
# 1. Load data
# ----------------------------------------------------------
ratings, movies, users = load_movielens_100k('data/ml-100k')

print("Ratings loaded:", ratings.shape)
print("Movies loaded:", movies.shape)
print("Users loaded:", users.shape)

# ----------------------------------------------------------
# 2. Create a simple holdout split:
#    For each user -> take 1 item to "test", rest to "train"
# ----------------------------------------------------------
held_out = {}
train_rows = []

for uid, group in ratings.groupby('user_id'):
    if len(group) < 2:
        continue

    # shuffle this user's ratings
    shuffled = group.sample(frac=1, random_state=42)

    # first item is held-out
    held_item = shuffled.iloc[0]
    held_out[uid] = {held_item["movie_id"]}

    # rest go into training set
    train_rows.append(shuffled.iloc[1:])

train_df = pd.concat(train_rows)
print("Train size:", train_df.shape)

# ----------------------------------------------------------
# 3. Train Surprise SVD on the training set
# ----------------------------------------------------------
print("\nTraining SVD model...")
algo, rmse = surprise_train_svd(
    train_df,
    n_factors=50,
    n_epochs=20
)
print("\nTraining finished.")
print("RMSE on training:", rmse)

# ----------------------------------------------------------
# 4. Evaluate Precision@10 per user
# ----------------------------------------------------------
precisions = []

print("\nEvaluating Precision@10...")
for uid, rel_items in held_out.items():
    recs = svd_recommend(algo, uid, movies, n=10)
    p = precision_at_k(recs, rel_items, k=10)
    precisions.append(p)

avg_precision = sum(precisions) / len(precisions)

print("\n-----------------------------------")
print("Final Evaluation Results")
print("-----------------------------------")
print("RMSE:", rmse)
print("Precision@10 (average):", avg_precision)
print("-----------------------------------")
