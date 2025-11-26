```markdown
# 🧠 02_Model_Training — Model Development & Training
Movie Recommendation System Project

---

## 📌 1. Introduction

This document covers the model building phase of the Movie Recommendation System using three approaches:

1. Matrix Factorization (SVD — Surprise Library)
2. Item-Based Collaborative Filtering
3. Content-Based Filtering (TF-IDF)

Each method contributes to the hybrid recommendation pipeline.

---

## 🟦 2. Matrix Factorization (SVD)

### ✔ Algorithm Used
**Singular Value Decomposition (SVD)** implemented using `Surprise`.

### ✔ Why SVD?
- Learns latent user & movie features  
- Performs well on sparse datasets  
- Strong rating prediction accuracy  

### ✔ Training Steps

1. Load ratings into `Dataset.load_from_df`.
2. Use `Reader(rating_scale=(1,5))`.
3. Fit the SVD model with parameters:
   - `n_factors=50`
   - `n_epochs=20`
4. Save trained model as:
```

models/svd_model.pkl

```

---

## 🟩 3. Item-Based Collaborative Filtering

### ✔ How it works
- Build a **user–item matrix** from ratings.
- Compute **item–item similarity** using cosine similarity.
- Recommend items most similar to previously rated movies.

### ✔ Key Functions
- `build_user_item_matrix()`
- `item_similarity_matrix()`
- `recommend_items_for_user()`

---

## 🟨 4. Content-Based Filtering (TF-IDF)

### ✔ Input Data
- Movie genres  
- Optional: descriptions or taglines (if available)

### ✔ Steps
1. Generate TF-IDF vectors  
2. Compute cosine similarity between movies  
3. Recommend content-wise similar movies  

---

## 🛠 5. Training Pipeline Summary

```

Load Data → Preprocess → Train SVD → Build Item-Based Model →
Build Content-Based Model → Save Artifacts

```

Artifacts generated:
- `svd_model.pkl` (MF model)
- Item similarity matrix (in memory)
- TF-IDF matrix (in memory)

---

## 🎯 6. Output
The following components are ready after training:
- Trained SVD collaborative filtering model  
- Item-based recommendation engine  
- Content-based similarity index  

These models feed into the evaluation and Flask API stages.


