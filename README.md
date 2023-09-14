# Movie_Recommendation_System

This Python script creates a movie recommendation system using content-based filtering. It leverages data from two CSV files, 'movies.csv' and 'credits.csv', to merge and preprocess movie information. The system calculates movie similarities based on tags, including genres, keywords, cast, and crew, and uses cosine similarity to provide personalized movie recommendations.

## Usage

1. Ensure you have the required libraries installed. You can install them using `pip`:

   pip install pandas scikit-learn
   
2. Run the script:
   
  python movie_recommendation.py

3. Enter a movie title, and the script will suggest similar movies based on content.

### Data Sources
'movies.csv': Contains movie details.
'credits.csv': Includes information about cast and crew.

## Recommendations
The recommendation system suggests movies similar to the one you input. It can be used for personalized movie recommendations, enhancing user experience on movie streaming platforms.

## Files
movie_recommendation.py: The main script.
movie_list.pkl: Pickle file storing preprocessed movie data.
similarity.pkl: Pickle file storing similarity data.
