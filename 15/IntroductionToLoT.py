import requests
import json
import time

API_KEY = "YOC1MXXSISVUZITD"
URL2 = "http://193.61.149.150:3000/channels/195/feeds.json?api_key=" + API_KEY


while True:
    time.sleep(0.1)
    r = requests.get(url=URL2)
    s = json.loads(r.content.decode("utf-8"))

    print(s["feeds"][-1]["field1"])
    if int(s["feeds"][-1]["field1"]) > 50:
        print("Dangerous!!!")
        break
    print("----------------------------")
