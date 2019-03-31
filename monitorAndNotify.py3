#log current time, temperature, and humidity to a database every minute. 
#Database options: SQLite 3 or MySQL.
#Script should run at startup automatically. Use cronjob, systemd service, run on boot in background etc.
#check against the config.json for values outside range and send notification
#push notification: Push bullet - 1 notification per day. - Use databse to remeber if notification sent or NOT. 
from sense_hat import SenseHat
import datetime,time,sqlite3
from datetime import timedelta

sense = SenseHat()
conn = sqlite3.connect('sensor.db')
cur = conn.cursor()

#create the table that stores sensor values
def createDB():
    #if not (cur.execute('SELECT name FROM sqlite_master WHERE type='table' AND name='sensor'')):
    cur.execute('''CREATE TABLE sensor(date datetime, temperature real, humidity real);''')

def getSensorData():
    humidity = round(sense.get_humidity(),2)
    temperature = round(sense.get_temperature(),2)
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
    print("%s" %humidity)
    print("%s" %temperature)
    print (st+"\n")
    cur.execute("INSERT INTO sensor VALUES(?,?,?)",st,temperature,humidity)

if __name__ == "__main__":
    #createDB()
    getSensorData()