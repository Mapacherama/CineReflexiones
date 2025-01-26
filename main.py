from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# Load and preprocess movie data
movies = pd.read_csv('data/movies.csv')

# Clean and preprocess the data
movies['genres'] = movies['genres'].fillna('[]')
movies['genres'] = movies['genres'].apply(eval).apply(lambda x: ', '.join([d['name'] for d in x if 'name' in d]))

@app.route('/api/movies', methods=['GET'])
def get_movies():
    # Return a subset of movie data as JSON
    return jsonify(movies[['title', 'genres', 'release_date', 'vote_average', 'revenue']].to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
