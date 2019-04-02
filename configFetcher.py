import json

with open("config.json", "r") as file:
    data = json.load(file)

def getMinTemperature():
    _ = data[0]['min_temperature']
    return _