import zmq as mq
import json
import urllib.request
from PIL import Image

context = mq.Context()
socket = context.socket(mq.REQ)
socket.connect("tcp://localhost:5555")
socket.send_string("Bloodborne: The Card Game")
message = json.loads(socket.recv())

if __name__ == "__main__":
    for dic in message:
        print(dic["name"])
        print(dic["thumbnail"])
        urllib.request.urlretrieve(
            dic["thumbnail"], "game_thumbnail.png"
        )
        img = Image.open("game_thumbnail.png")
        img.show()
