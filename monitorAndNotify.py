from sense_hat import SenseHat
import datetime
import time
from datetime import timedelta

sense = SenseHat()

while True:
    humidity = round(sense.get_humidity(),2)
    temperature = round(sense.get_temperature(),2)
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print("%s" %humidity)
    print("%s" %temperature)
    print (st+"\n")
    time.sleep(1)
