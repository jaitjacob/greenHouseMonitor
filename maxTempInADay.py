import sqlite3
from datetime import datetime, timedelta

DB_NAME = "sensor.db"
DATE_FORMAT = "%Y-%m-%d"
ONE_DAY_DELTA = timedelta(days = 1)

class Alerter:

    def getMaxTempToday():
        connection = sqlite3.connect(DB_NAME)
        connection.row_factory = sqlite3.Row
        with connection:
            cursor = connection.cursor()
    #row = cursor.execute("SELECT DATE(MIN(date)), DATE(MAX(date)) FROM sensor").fetchone()
    #startDate = datetime.strptime(row[0], DATE_FORMAT)
    #endDate = datetime.strptime(row[1], DATE_FORMAT)
    #print("Dates:")
    #date = startDate
    #while date <= endDate:
            row = cursor.execute(
                 """SELECT MAX(temperature) FROM sensor
                    WHERE date >= DATE('now')""").fetchone()            
            print(" | Row Count: " + str(row[0]))        
        connection.close()



# Execute program.
if __name__ == "__main__":
    maxTemp = Alerter()
    maxTemp
