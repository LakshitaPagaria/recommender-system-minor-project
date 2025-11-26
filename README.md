# 🎬 Movie Recommender System  
### Hybrid Collaborative + Content-Based Recommendation Engine  
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-API-orange)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Completed-success)

---

## 📖 Project Overview

This project implements a **Movie Recommendation System** powered by:

- 🔷 **Matrix Factorization (SVD – Surprise Library)**  
- 🟩 **Item-Based Collaborative Filtering**  
- 🟨 **Content-Based Filtering using TF-IDF**  
- 🚀 **Flask API for real-time movie recommendations**

The system uses the **MovieLens 100k dataset** and delivers personalized Top-N movie suggestions for any user.

---

## 📌 Features

### 🔹 **1. Matrix Factorization (SVD)**
- Learns latent factors for users & movies  
- Predicts ratings  
- Generates personalized recommendations  

### 🔹 **2. Item-Based Collaborative Filtering**
- Builds user–item interaction matrix  
- Computes item–item similarity  
- Suggests similar movies based on history  

### 🔹 **3. Content-Based Filtering**
- Uses TF-IDF features from genres  
- Recommends similar movies based on content  

### 🔹 **4. REST API using Flask**
Endpoint:

```

/recommend?user_id=<id>&n=<count>

```

Returns movie titles in JSON format.

---

## 📂 Project Structure

```

recommender_system/
│
├── app/
│   └── app.py                 # Flask API
│
├── src/
│   ├── data_prep.py           # Load and preprocess MovieLens data
│   ├── mf_surprise.py         # SVD MF model (Surprise)
│   ├── cf_item_based.py       # Item-based CF
│   ├── content_based.py       # TF-IDF content model
│   └── eval_metrics.py        # Precision@K, evaluation utilities
│
├── models/
│   └── svd_model.pkl          # Saved SVD model (generated after training)
│
├── data/
│   └── ml-100k/               # MovieLens dataset
│
├── run_quick_demo.py          # Train SVD and save model
├── eval_svd.py                # Evaluate SVD (RMSE, Precision@K)
└── requirements.txt           # Python package dependencies

````

---

## 🔧 Installation

### **1️⃣ Clone the Repository**
```bash
git clone https://github.com/<your-username>/recommender-system-minor-project.git
cd recommender-system-minor-project
````

### **2️⃣ Create a Virtual Environment**

```bash
python -m venv venv311
```

Activate it:

```bash
venv311\Scripts\activate
```

### **3️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## 📘 Usage

### **▶ 1. Train the SVD Model**

```bash
python run_quick_demo.py
```

This will:

* Train SVD on MovieLens
* Save model → `models/svd_model.pkl`

### **▶ 2. Start Flask API**

```bash
python app/app.py
```

Visit in browser:

```
http://127.0.0.1:5000/recommend?user_id=1&n=10
```

Example JSON output:

```json
{
  "recommendations": [
    "Usual Suspects, The (1995)",
    "Star Wars (1977)",
    "Pulp Fiction (1994)",
    "Fargo (1996)",
    "Godfather, The (1972)",
    "Wrong Trousers, The (1993)",
    "Raiders of the Lost Ark (1981)",
    "Close Shave, A (1995)",
    "Casablanca (1942)",
    "Third Man, The (1949)"
  ],
  "user_id": 1
}
```

---

## 📊 Evaluation

Run:

```bash
python eval_svd.py
```

### **Results:**

| Metric           | Value    |
| ---------------- | -------- |
| **RMSE**         | `0.9403989197241039`   |
| **Precision@10** | `0.0024390243902439033` |

---

## 🧠 Algorithms Used

### 🔷 Matrix Factorization (SVD – Surprise)

* Learns hidden features for users/movies
* Predicts missing ratings

### 🟩 Item-Based Collaborative Filtering

```
User–Item Matrix → Item–Item Similarity → Top-N Recommendations
```

### 🟨 Content-Based TF-IDF

```
Genres → TF-IDF → Similarity → Recommendations
```

---

## 🏗 System Architecture

```
MovieLens Data
     ↓
Data Preprocessing (src/data_prep.py)
     ↓
Model Training (SVD / Item-Based / Content-Based)
     ↓
Model Saved → models/svd_model.pkl
     ↓
Flask API Loads Model
     ↓
User Request → /recommend
     ↓
Top-N Movie Recommendations (JSON)
```

---

## 🎥 Example Outputs

### **Item-Based CF Output**

```
[423, 655, 568, 403, 385, ...]
```

Mapped to titles:

```
Schindler's List  
Clueless  
True Lies  
Batman  
E.T.  
```

### **Content-Based Output**

```
Aladdin, Pocahontas, Balto, Gumby, ...
```

---

## 📌 Requirements

* Python 3.11
* numpy, pandas, scikit-learn
* surprise
* flask
* tqdm

Install via:

```bash
pip install -r requirements.txt
```

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Acknowledgements

* **MovieLens Dataset** – GroupLens Research
* **Surprise Library** – N. Hug
* **scikit-learn**

---

# 🎉 Thank You!

If you like this project, give it a ⭐ on GitHub!
