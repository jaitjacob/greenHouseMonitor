import json

with open("config.json", "r") as file:
    data = json.load(file)

def getMinTemperature():
    _ = data[0]['min_temperature']
    return _

def getMaxTemperature():
    _ = data[0]['max_temperature']
    return _

def getMinHumidity():
    _ = data[0]['min_humidity']
    return _
        
def getMaxHumidity():
    _ = data[0]['max_humidity']
    return _