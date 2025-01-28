from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import ast

app = Flask(__name__)
CORS(app)  # Enable cross-origin requests

# Load and preprocess movie data
movies = pd.read_csv('data/movies.csv')
# Drop rows with any NaN values
movies_cleaned = movies.dropna()

# Optional: Reset the index after dropping rows
movies_cleaned.reset_index(drop=True, inplace=True)

def extract_genres(genre_str):
    try:
        # Convert the string to a list of dictionaries
        genres = ast.literal_eval(genre_str)
        # Extract the 'name' values and join them as a comma-separated string
        return ', '.join([genre['name'] for genre in genres if 'name' in genre])
    except (ValueError, SyntaxError):
        # Return an empty string if there's an error in parsing
        return ''

# Clean and preprocess the data
movies['genres'] = movies['genres'].apply(extract_genres)
movies['release_date'] = pd.to_datetime(movies['release_date'], errors='coerce').dt.strftime('%Y-%m-%d')

@app.route('/api/movies', methods=['GET'])
def get_movies():
    # Return a subset of movie data as JSON
    return movies_cleaned[['title', 'genres', 'release_date', 'vote_average', 'revenue']].to_dict(orient='records')

if __name__ == '__main__':
    app.run(debug=True)
