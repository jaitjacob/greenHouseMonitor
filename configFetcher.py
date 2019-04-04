import json

with open("config.json", "r") as file:
    data = json.load(file)

def getMinTemperature():
    """ Fetches the minimum temperature from the config file """
    _ = data[0]['min_temperature']
    return _

def getMaxTemperature():
    """ Fetches the maximum temperature from the config file """
    _ = data[0]['max_temperature']
    return _

def getMinHumidity():
    """ Fetches the minimum humidity from the config file """
    _ = data[0]['min_humidity']
    return _
        
def getMaxHumidity():
    """ Fetches the maximum humidity from the config file """
    _ = data[0]['max_humidity']
    return _