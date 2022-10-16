# Movie Recommender Systems

This repository contains two recommender systems that I implemented. The first one utilizes content based filtering (completed) and the second one utilizes collaborative filtering (uncompleted).

# Recommender with Content Based Filtering

## Model
This recommender model uses cosine similarity with linear_kernel method from sklearn.metrics.pairwise to retrieve similar movies. First hundred movies are scored from 100 to 1. Then it uses movie genres for re-scoring. For each matching genre movie is awarded 10 scores and it loses 2 scores otherwise. Best scoring ten movies are displayed to the user.

## Data
[“MPST: Movie Plot Synopses with Tags”](https://www.kaggle.com/datasets/cryptexcode/mpst-movie-plot-synopses-with-tags) dataset has been used for this model. This dataset contains 13757 unique movies with their plot synopsis and genres.

## Usage

Uncomment lines to download the data and extra requirements. Run the whole notebook. Add new cell for recommendation with this function:
```python
recommend_movie(movie_name)
```

## Results
Even though movie recommendation is a rather subjective topic this model's recommendations are fairly different from other recommenders on the web. There might be two main reasons for that: \
First one is that this model mainly depends on the movie plots. So similar plots with different settings might be getting more scores than others. It might be an interesting experiment to watch the recommended movies and try to catch plot similarities. (If you have enough free time and don't have too much movie on your watchlist please don't refrain to try this and share your results with me.) \
\
The other reason is that the model doesn't account for ratings and other metadata. Most of the models push back movies with lower ratings to increase accuracy. Even though some movies randomly pops up, with this approach one can say that movies with lower ratings have a chance to be recommended too. This can be used for more sophisticated audience that wants to explore new movies.\
\
Recommendations for top ten movies from IMDB's TOP 250 list are also included at the end of the notebook. Sequels are excluded to provide more diversity and "The Good, the Bad and the Ugly" is also excluded because I don't think it is in the dataset.

# Recommender with Collaborative Filtering 
Work on progress...
## Model
This recommender model's aim is to use genres that movies belong to and average ratings of users for each genre. These vectors are (hopefully) embedded and passed through dense layers. Then results are (supposedly) multiplicated using matrix multiplication and compared with actual ratings of users for the individual movies.
## Data
[MovieLens Latest Datasets](https://grouplens.org/datasets/movielens/latest/) dataset contains user ratings, movie names and movie genres.
## Usage
None yet
## Results
Currently model only outputs a matrix of nan's. I'm currently working on debugging and developing other features. I would really appreciate any help about debugging, embedding vectors and matrix multiplication to create a complete matrix of ratings.
## License
None
