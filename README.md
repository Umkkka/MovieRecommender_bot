# Movie-recommender-bot
Telegram bot that implements one of the ML techniques for generating movie recommendations

Bot that accepts the name of a movie as input, and returns a list with similar movies to the one you entered. To generate similar movies, we used a tool provided by the sklearn library, CountVectorizer. The sample with movie data is analyzed, then the text is converted to vectors. After that, there is a similarity between them.


bot.py - main file
recommend_system.py - file with generating recommendations
IMDB.csv - dataset with movie data

In the near future:
- The movie dataset will be replaced. A selection with more movies and more information about them will be added
- The output of the recommendation will be implemented in a consumer-oriented form
- Other edits will be made
