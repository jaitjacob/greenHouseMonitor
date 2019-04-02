#!/usr/bin/env python3
import requests,json,os,sqlite3
from datetime import datetime, timedelta

class pushNotify:
    def createDB(self):
        conn = sqlite3.connect('sensor.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE notified(notifieddates datetime);''')

    def checkIfNotifiedToday(self):
        DATE_FORMAT = "%Y-%m-%d"
        conn = sqlite3.connect('sensor.db')
        cur = conn.cursor()
        row = cur.execute("SELECT DATE(MAX(notifieddates)) FROM notified").fetchone()
        recentDate = datetime.strptime(row[0], DATE_FORMAT)
        recentDate = recentDate.strftime(DATE_FORMAT)
        now = datetime.now()
        now = now.strftime(DATE_FORMAT)

        if(recentDate == now):
            print("notification already sent for the day")
        else:
            print("executing push notification code")

    def configCheck(self):
        

# Execute.
if __name__ == "__main__":
    pushNotifyObj = pushNotify()
    #pushNotifyObj.createDB()
    pushNotifyObj.checkIfNotifiedToday()
