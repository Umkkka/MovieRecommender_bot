# Movie-recommender-bot
Telegram bot that implements one of the ML techniques for generating movie recommendations

Bot that accepts the name of a movie as input, and returns a list with similar movies to the one you entered. To generate similar movies, we used a tool provided by the sklearn library, CountVectorizer. The sample with movie data is analyzed, then the text is converted to vectors. After that, there is a similarity between them.
