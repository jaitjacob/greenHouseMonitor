#log current time, temperature, and humidity to a database every minute. 
#Database options: SQLite 3 or MySQL.
#Script should run at startup automatically. Use cronjob, systemd service, run on boot in background etc.
#check against the config.json for values outside range and send notification
#push notification: Push bullet - 1 notification per day. - Use databse to remeber if notification sent or NOT. 
from sense_hat import SenseHat
import datetime
import time
from datetime import timedelta

sense = SenseHat()


def get_humidity():
    return humidity = round(sense.get_humidity(),2)

def get_temperature():
    return temperature = round(sense.get_temperature(),2)

def get_time():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    return st



#print("%s" %humidity)
#print("%s" %temperature)
#print (st+"\n")