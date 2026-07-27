# Movie Recommendation System

## Objective
The primary objective of this project is to build a content-based Movie Recommendation System using Machine Learning and Natural Language Processing (NLP) techniques. The system analyzes movie metadata—such as genres, keywords, taglines, cast, and directors—to recommend titles similar to a user's favorite movie.

## Dataset Link
* *Dataset:* [Movies CSV Dataset on Kaggle](https://www.kaggle.com/datasets/harshshinde8/movies-csv)

## Libraries Used
* *pandas*: Used for data loading, manipulation, and cleaning missing values.
* *scikit-learn*:
  * TfidfVectorizer: Transforms textual metadata into numerical feature vectors.
  * NearestNeighbors: ML model used to find similar movies based on cosine distance.
* *kagglehub*: Automates dataset downloading directly into the Google Colab environment.
* *difflib*: Standard Python module used for string matching to handle slight user typos in movie titles.

## Methodology
1. *Data Preprocessing:*
   * Textual metadata features (genres, keywords, tagline, cast, director) are selected from the dataset.
   * Missing values (NaN) are replaced with empty strings.
   * All selected attributes are combined into a unified text feature string for each movie.
2. *Text Vectorization:*
   * The combined text data is passed through TfidfVectorizer to produce a high-dimensional TF-IDF feature matrix.
3. *Model Training:*
   * An unsupervised NearestNeighbors model configured with metric="cosine" and algorithm="brute" is fitted on the TF-IDF feature vectors.
4. *Recommendation Generation:*
   * The user enters a movie title, which is matched against dataset entries using difflib.get_close_matches.
   * The vector of the matched movie is queried against the NearestNeighbors model to retrieve the nearest vector points.
   * The corresponding movie titles are displayed as final recommendations.

## Results
* Given an input movie (e.g., *"Avatar"*), the system successfully processes the metadata and returns the top 5 most similar movies based on shared genre tags, plot keywords, directing style, and cast line-up.
* The model efficiently handles typos and returns fast, scalable vector distance searches using K-Nearest Neighbors.

## Conclusion
This content-based recommendation system demonstrates how unsupervised machine learning algorithms (K-Nearest Neighbors) combined with NLP techniques (TF-IDF) can effectively process text metadata to generate personalized recommendations without requiring historical user interaction or rating data.
