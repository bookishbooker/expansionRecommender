# expansionRecommender
## Program Usage
### This expansion recommendation program uses expansionRecommender.py as a server. It accepts strings representing the names of board games as requests and uses the function from bgg_game_finder.py to search a .csv database containing a majority of the boardgame data hosted on the website BoardGameGeek.com. It uses the data from said data base to parse xml data from the website and return the titles, average rating, thumbnails, and link to any expansions for the requested boardgame.
## Requesting and Recieving Data
### This microservice uses ZeroMQ running locally on your computer. The client must send the server a string representing the name of a boardgame. For example: "CATAN". If the title of the board game is not found in the database .csv file, the service will send back text indicating that the game wasn't found.

