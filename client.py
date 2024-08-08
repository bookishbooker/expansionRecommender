import zmq as mq
import json

context = mq.Context()
socket = context.socket(mq.REQ)
socket.connect("tcp://localhost:5555")
socket.send_string("CATAN")
message = json.loads(socket.recv())
for dic in message:
    print(dic["name"])
