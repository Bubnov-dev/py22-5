import requests

city_name = input("Enter city name: ")
r = requests.get(
    "https://api.openweathermap.org/data/2.5/weather?q=" + city_name + "&APPID=ae3fbb8bfd9b266f069058de6ae9c738").json()
print("Weather: ", r['weather'])
print("Humidity: ", r['main']['humidity'])
print("Pressure: ", r['main']['pressure'])
