# 📝 01_EDA — Exploratory Data Analysis  
Movie Recommendation System Project

---

## 📌 1. Introduction

This document summarizes the Exploratory Data Analysis (EDA) performed on the **MovieLens 100k dataset** used for building the Movie Recommendation System.  
The EDA helps understand the structure of the data, user behavior, movie popularity, genre distribution, and the overall sparsity of the dataset.

---

## 📂 2. Dataset Description

The MovieLens 100k dataset contains:

- **100,000 ratings**
- **943 users**
- **1,682 movies**
- Rating scale: **1 to 5**
- Metadata includes:  
  - Movie titles  
  - Release year  
  - Genres  
  - User demographic info (optional)

The following files are used:

| File | Description |
|------|-------------|
| `u.data` | User–Movie ratings |
| `u.item` | Movie details & genres |
| `u.user` | User demographic data |

---

## ⭐ 3. Rating Distribution

Understanding rating distribution helps identify:

- Average user rating behavior  
- Bias toward certain rating values  
- Usefulness of normalization  

**Key Observations:**

- Ratings are mostly between **3 and 4**
- Users rarely rate movies with 1 or 5
- The distribution is slightly right-skewed

This supports the use of **matrix factorization** techniques.

---

## 👥 4. User Activity Analysis

To understand how active each user is:

- Count number of ratings per user  
- Identify high-activity vs. low-activity users  

**Findings:**

- Only a few users are highly active (100+ ratings)  
- Most users rated fewer than **50 movies**  
- Activity imbalance can affect collaborative filtering

---

## 🎬 5. Movie Popularity Analysis

To understand how often movies are rated:

- Count number of ratings per movie  
- Identify popular movies (high number of ratings)  
- Observe rarely-rated movies  

**Insights:**

- Popular movies include:  
  _Star Wars, Contact, Men in Black, Fargo_  
- Many movies have very few ratings  
- Long-tail effect is clearly visible

---

## 🎭 6. Genre Distribution

Genres help with Content-Based Filtering.

**Analysis includes:**

- Frequency count of genre labels  
- Genre-based movie diversity  

**Observations:**

- Most common genres:  
  - **Drama, Comedy, Action**
- Less common:  
  - Documentary, Film-Noir, Western  

Movies often belong to **multiple genres**, increasing content richness.

---

## 🔢 7. User–Item Sparsity

The sparsity of the rating matrix deeply affects CF and MF performance.

- Total possible ratings = 943 × 1682 = **1,585,726**
- Actual ratings = **100,000**

### 🔹 Sparsity ≈ **93.7%**

Meaning:

- Most user–movie interactions are **missing**
- Justifies:
  - Collaborative Filtering  
  - Matrix Factorization  
  - Content-based augmentation  

---

## 🔗 8. Correlation & Similarity Analysis

During EDA, we observe:

- **Popular movies** tend to have stronger similarity signals  
- Users show consistent rating habits  
- Movie–movie similarity matrices are sparse but informative  

This confirms that **item-based CF** will perform reasonably well.

---

## 📘 9. Summary of Key Insights

- Ratings are moderately high (avg ~3.5)  
- Data is **highly sparse**, ideal for SVD  
- User activity varies widely  
- Popular movies dominate rating frequency  
- Genres provide strong content signals  
- EDA supports the hybrid modeling approach used in the project

---

## 🚀 10. Next Steps

After EDA, the workflow proceeds to:

1. Data preprocessing  
2. Building recommendation models  
3. Training SVD (Surprise)  
4. Evaluating using RMSE + Precision@10  
5. Deploying the model via Flask API  

---
