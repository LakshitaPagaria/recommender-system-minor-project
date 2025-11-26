````markdown
# 🌐 04_API_Documentation — Flask API Guide
Movie Recommendation System Project

---

## 📌 1. Overview

The project includes a **Flask REST API** that serves real-time movie recommendations using the trained SVD model.

The API loads:
- The saved SVD model (`svd_model.pkl`)
- Movie metadata (`movies.csv`)

---

## 📡 2. Running the API

Start the server:

```bash
python app/app.py
````

Localhost endpoint:

```
http://127.0.0.1:5000/
```

---

## 🔗 3. Recommendation Endpoint

### **GET /recommend**

```
/recommend?user_id=<id>&n=<count>
```

### ✔ Parameters

| Parameter | Type | Required | Description                              |
| --------- | ---- | -------- | ---------------------------------------- |
| `user_id` | int  | Yes      | User to recommend movies for             |
| `n`       | int  | No       | Number of recommendations (default = 10) |

---

## 📥 Example Request

```
http://127.0.0.1:5000/recommend?user_id=1&n=10
```

---

## 📤 Example JSON Response

```json
{
  "user_id": 1,
  "recommendations": [
    "Star Wars (1977)",
    "Pulp Fiction (1994)",
    "Contact (1997)",
    "Men in Black (1997)"
  ]
}
```

---

## ❗ Error Handling

If model file is missing:

```json
{
  "error": "Model file not found"
}
```

If invalid user_id:

```json
{
  "recommendations": []
}
```

---

## 🚀 4. API Architecture

```
Client Request
      ↓
Flask Endpoint (/recommend)
      ↓
Load Model + Movies Data
      ↓
Generate Top-N Recommendations
      ↓
Return JSON Response
```

---

## 📝 5. Summary

The Flask API:

* Serves real-time recommendations
* Uses the trained SVD model
* Returns results in clean JSON format
* Can be extended into a full frontend application

---


