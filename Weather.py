import requests

api_address = "http://api.openweathermap.org/data/2.5/forecast?id=1264733&appid=#"

json_data = requests.get(api_address).json()


def temperature():
    temperature_celsius = round(json_data['list'][0]['main']['temp'] - 273, 1)
    return temperature_celsius


def description():
    descriptions = json_data['list'][0]['weather'][0]['description']
    return descriptions
