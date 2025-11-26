import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

def build_movie_profiles(movies_df):
    """
    Creates a 'soup' combining title + genres (for ML-100k genres are binary columns).
    Returns tfidf_matrix and the movies_df (with 'soup' added).
    """
    genre_cols = ['unknown','Action','Adventure','Animation',"Children's",'Comedy','Crime','Documentary','Drama',
                  'Fantasy','Film-Noir','Horror','Musical','Mystery','Romance','Sci-Fi','Thriller','War','Western']
    if set(genre_cols).issubset(movies_df.columns):
        movies_df['genres'] = movies_df[genre_cols].apply(lambda x: ' '.join([g for g in genre_cols if x[g]==1]), axis=1)
    movies_df['soup'] = movies_df['title'].fillna('') + ' ' + movies_df.get('genres','').fillna('')
    tfidf = TfidfVectorizer(stop_words='english')
    tfidf_matrix = tfidf.fit_transform(movies_df['soup'])
    return tfidf_matrix, movies_df

def content_recommend(movie_id, tfidf_matrix, movies_df, top_n=10):
    idxs = movies_df.index[movies_df['movie_id'] == movie_id].tolist()
    if not idxs:
        return []
    idx = idxs[0]
    cosine_sim = linear_kernel(tfidf_matrix[idx:idx+1], tfidf_matrix).flatten()
    related_idx = cosine_sim.argsort()[::-1][1:top_n+1]
    return movies_df.iloc[related_idx]['movie_id'].tolist()
