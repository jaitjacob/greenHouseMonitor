#!/usr/bin/env python3

#log current time, temperature, and humidity to a database every minute. 
#Database options: SQLite 3 or MySQL.
#Script should run at startup automatically. Use cronjob, systemd service, run on boot in background etc.
#check against the config.json for values outside range and send notification
#push notification: Push bullet - 1 notification per day. - Use databse to remeber if notification sent or NOT. 

from sense_hat import SenseHat
import datetime,time,sqlite3,configFetcher, notifyChecker,pushNotify
from datetime import timedelta
import pdb

sense = SenseHat()

class monitor:
#create the table that stores sensor values
    def createDB(self):
        conn = sqlite3.connect('sensor.db')
        cur = conn.cursor()
        #if not (cur.execute('SELECT name FROM sqlite_master WHERE type='table' AND name='sensor'')):
        cur.execute('''CREATE TABLE sensor(date datetime, temperature real, humidity real);''')

    def getSensorData(self):
        humidity = round(sense.get_humidity(),2)
        temperature = round(sense.get_temperature(),2)
        print("%s" %humidity)
        print("%s" %temperature)
        return humidity, temperature

    def checkData(self, currentTemp, currentHum):
        #conn = sqlite3.connect('sensor.db')
        #cur = conn.cursor()
        maxTemp = configFetcher.getMaxTemperature()
        minTemp = configFetcher.getMinTemperature()
        maxHum = configFetcher.getMaxHumidity()
        minHum = configFetcher.getMaxHumidity()
        print(maxTemp,maxHum,minTemp,minHum)
        message = ""
        shouldNotify = 0
    
        if(currentTemp>maxTemp):
            message = message+"current temperature exceeds configured temperature. "
            shouldNotify = 1
        
        if(currentTemp<minTemp):
            message = message+"current temperature is below configured temperature. "
            shouldNotify = 1

        if(currentHum>maxHum):
            message = message+"current humidity exceed configured humidity. "
            shouldNotify = 1

        if(currentHum<minHum):
            message = message+"current humidity is below configured humidity. "
            shouldNotify = 1
        pdb.set_trace()
        print(message)
        
        if(shouldNotify==1):
            if(notifyChecker.checkIfNotifiedToday(self)):
                print("sending push notification.")
                pushNotify.send_notification_via_pushbullet("GreenHouse Alert",message)
                self.insertDataToDB(currentTemp,currentHum)
                notifyChecker.insertNotifiedDate(self)
        else:
            print("Already notified for the day.")
            self.insertDataToDB(currentTemp,currentHum)

    def insertDataToDB(self, currentTemp, currentHum):
        conn = sqlite3.connect('sensor.db')
        cur = conn.cursor()
        
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        print (st+"\n")
        
        cur.execute("INSERT INTO sensor values((?),(?),(?))", (currentTemp,currentHum,st))
        conn.commit()
        conn.close()


if __name__ == "__main__":
    monitorObj = monitor()
    currentTemp, currentHum = monitorObj.getSensorData()
    monitorObj.checkData(currentTemp, currentHum)

