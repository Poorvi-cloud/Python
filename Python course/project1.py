# Weather app

import requests
import json

city = input("enter the name of the city\n: ")

url = "https://api.weatherapi.com/v1/current.json?key=56e3893dd0854c68af3184422242811&q={city}"

r = requests.get(url)
print(r.text)
