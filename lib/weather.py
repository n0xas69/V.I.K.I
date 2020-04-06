"""
Utilise les API suivantes :
https://ipinfo.io/
https://openweathermap.org/
"""

import requests

def get_town():
    token = "ac72ecb20d21e7"
    data = {"token" : token}
    apiResp = requests.get("https://ipinfo.io", params=data)
    city = apiResp.json()
    return city.get("city")

def get_weather(town):
    data = {"q" : town, "appid" : "d5bf68d126c5eda93e8ee691ce3ddcc2"}
    weaver = requests.get("https://api.openweathermap.org/data/2.5/weather", params=data)
    temp = weaver.json()
    w = temp.get("main")
    t = w.get("temp") - 273.15 # conversion en degré celcius
    return format(t, ".0f")

if __name__ == "__main__":
    city = get_town()
    temp = get_weather(city)
    print(f"Il fait {temp}° à {city}")