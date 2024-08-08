import csv_search as search
import zmq as mq
import requests as req
import xml.etree.ElementTree as Et

context = mq.Context()
socket = context.socket(mq.REP)
socket.bind("tcp://*:5555")

while True:
    message = socket.recv()
    search_id = search.search_by_name(message.decode())
    if search_id is None:
        socket.send_string("Game not found")
        print("whoops")
    else:
        search_id = str(search_id.loc[0, "bgg_id"])
        url = f"https://boardgamegeek.com/xmlapi2/thing?id={search_id}"
        game_object = req.get(url)
        game_object = Et.fromstring(game_object.content)
        expansion_list = []
        high = -1
        middle = -1
        low = -1
        popular1 = None
        popular2 = None
        popular3 = None
        for link in game_object[0].findall('link'):
            if link.get('type') == 'boardgameexpansion':
                expansion_id = link.get('id')
                url = f"https://boardgamegeek.com/xmlapi2/thing?id={expansion_id}&stats=1"
                expansion_xml = req.get(url)
                expansion_data = Et.fromstring(expansion_xml.content)
                try:
                    bayes_avg = float(expansion_data[0].find("statistics").find("ratings").find("bayesaverage").get("value"))
                except:
                    bayes_avg = 0
                if bayes_avg < low:
                    continue
                else:
                    name = expansion_data[0].find("name").get("value")
                    thumbnail = expansion_data[0].find("thumbnail")
                    link = f"https://boardgamegeek.com/boardgameexpansion/{expansion_id}"
                    expansion_object = {
                        "name": str(name),
                        "thumbnail": str(thumbnail),
                        "rating": bayes_avg,
                        "link": link
                    }
                    if bayes_avg > high:
                        popular3 = popular2
                        popular2 = popular1
                        popular1 = expansion_object
                        high = bayes_avg
                    elif bayes_avg > middle:
                        popular3 = popular2
                        popular2 = expansion_object
                        middle = bayes_avg
                    else:
                        popular3 = expansion_object
                        low = bayes_avg
        rec_list = []
        if popular1 is not None:
            rec_list.append(popular1)
        if popular2 is not None:
            rec_list.append(popular2)
        if popular3 is not None:
            rec_list.append(popular3)

        socket.send_json(rec_list)
        print("done")
