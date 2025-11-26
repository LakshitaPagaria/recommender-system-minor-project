from flask import Flask, request, jsonify
import joblib, os, pandas as pd

app = Flask(__name__)
DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data', 'ml-100k')

# minimal movie loader
try:
    MOVIES = pd.read_csv(os.path.join(DATA_DIR, 'u.item'), sep='|', encoding='latin-1', header=None)
    MOVIES = MOVIES[[0,1]]
    MOVIES.columns = ['movie_id','title']
except Exception:
    MOVIES = pd.DataFrame({'movie_id':[], 'title':[]})

MODEL_PATH = os.path.join(os.path.dirname(__file__), '..', 'models', 'svd_model.pkl')
if os.path.exists(MODEL_PATH):
    algo = joblib.load(MODEL_PATH)
else:
    algo = None

@app.route('/recommend', methods=['GET'])
def recommend():
    user_id = int(request.args.get('user_id', 1))
    n = int(request.args.get('n', 10))
    if algo is None or MOVIES.empty:
        return jsonify({'user_id': user_id, 'recommendations': []})
    preds = []
    for mid in MOVIES['movie_id'].unique():
        try:
            est = algo.predict(user_id, mid).est
            preds.append((mid, est))
        except:
            continue
    preds.sort(key=lambda x: x[1], reverse=True)
    top_ids = [p[0] for p in preds[:n]]
    titles = MOVIES[MOVIES['movie_id'].isin(top_ids)]['title'].tolist()
    return jsonify({'user_id': user_id, 'recommendations': titles})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
