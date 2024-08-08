# expansionRecommender
## Program Usage
This expansion recommendation program uses expansionRecommender.py as a server. It accepts strings representing the names of board games as requests and uses the function from bgg_game_finder.py to search a .csv database containing a majority of the boardgame data hosted on the website BoardGameGeek.com. It uses the data from said data base to parse xml data from the website and return the titles, average rating, thumbnails, and link to the game's three most popular expansions as a list of dictionaries.
## Requesting and Recieving Data
This microservice uses ZeroMQ running locally on your computer. The client must send the server a string representing the name of a boardgame. For example: "CATAN". If the title of the board game is not found in the database .csv file, the service will send back text indicating that the game wasn't found.

To create a server to receive and process requests, please reference the following code:
#### context = zmq.Context()
#### socket = context.socket(zmq.REP)
#### socket.bind("tcp://*5555")

To create a client to send requests, please reference the following code:
#### context = zmq.Context()
#### socket = context.socket(zmq.REQ)
#### socket.connect("tcp://localhost:5555:")
#### socket.send_string("Board Game Name")
#### expansion_info = json.loads(socket.recv())
