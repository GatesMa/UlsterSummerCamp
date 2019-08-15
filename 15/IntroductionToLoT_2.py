import requests
import time
import random
API_KEY = "OPXO9K519UGWM951"
while 1:
  time.sleep(10)
  value = str(random.randint(0,40))
  print("temperature is : " + value)
  URL = "http://193.61.149.150:3000/update?api_key=" + API_KEY + "&field1=" + value
  r = requests.post(url=URL)
