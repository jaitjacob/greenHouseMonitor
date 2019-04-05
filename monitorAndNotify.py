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
    """
    This is the monitor class. The objects of this class performs the core functions of the Green House Monitor which
    includes but is not limited to getting sensor values, checking them against the configuration files, calling the push
    notification function and utimately saving required data to the database.
    """
    def createDB(self):
        """
        This peice of code is only ran once in the entire lifecycle of the code. Its main purpose is to create the
        necessary table within a databse.
        """
        conn = sqlite3.connect('sensor.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE sensor(date datetime, temperature real, humidity real);''')

    def getSensorData(self):
        """This function read the humidity and temperature value from the Sense Hat and returns it to the caller"""
        humidity = round(sense.get_humidity(),2)
        temperature = round(sense.get_temperature(),2)
        print("%s" %humidity)
        print("%s" %temperature)
        return humidity, temperature

    def checkData(self, currentTemp, currentHum):
        """This function fetches all the values saved in the config.json file and compares them to the current
        temperature and humidity readings received via the SenseHat. Approporiate message is generated and a decision
        where to send a push notification is made.
        """
        maxTemp = configFetcher.getMaxTemperature()
        minTemp = configFetcher.getMinTemperature()
        maxHum = configFetcher.getMaxHumidity()
        minHum = configFetcher.getMaxHumidity()
        
        #Config.json file values
        #print(maxTemp,maxHum,minTemp,minHum)
        
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
        
        #pdb.set_trace()
        #The above line of code is just for debugging. Uncomment if you want it back as your breakpoint.
        print(message)
        
        if(shouldNotify==1):
            if(notifyChecker.checkIfNotifiedToday(self)==1):
                print("sending push notification.")
                pushNotify.send_notification_via_pushbullet("GreenHouse Alert",message)
                self.insertDataToDB(currentTemp,currentHum)
                notifyChecker.insertNotifiedDate(self)
            else:
                print("Already notified for the day.")
                self.insertDataToDB(currentTemp,currentHum)

    def insertDataToDB(self, currentTemp, currentHum):
        """Data that needs to be saved to the databse is finally inserted into the tables within the sensor.db database.
        All the data is committed and a safe connection close procedure is performed to maintain the integrity of the database.
        """
        conn = sqlite3.connect('sensor.db')
        cur = conn.cursor()
        #when its time to insert the sensor values to the database add the timestamp as well with it.
        ts = time.time()
        st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        
        cur.execute("INSERT INTO sensor values((?),(?),(?))", (st,currentTemp,currentHum))
        conn.commit()
        conn.close()


if __name__ == "__main__":
    monitorObj = monitor()
    currentTemp, currentHum = monitorObj.getSensorData()
    monitorObj.checkData(currentTemp, currentHum)

