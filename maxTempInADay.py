import sqlite3
from datetime import datetime, timedelta

DB_NAME = "sensor.db"
DATE_FORMAT = "%Y-%m-%d"
ONE_DAY_DELTA = timedelta(days = 1)

class Alerter:

    def getMaxTempToday(self):
        connection = sqlite3.connect(DB_NAME)
        connection.row_factory = sqlite3.Row
        with connection:
            cursor = connection.cursor()
            row = cursor.execute(
                 """SELECT MAX(temperature) FROM sensor
                    WHERE date >= DATE('now')""").fetchone()            
            if(str):
            print(str(row[0]))        
        connection.close()



# Execute program.
if __name__ == "__main__":
    maxTemp = Alerter()
    maxTemp.getMaxTempToday()
