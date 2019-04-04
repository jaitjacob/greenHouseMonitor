#!/usr/bin/env python3
import requests
import json
import os
import sqlite3
from datetime import datetime, timedelta
import pushNotify
import configFetcher


def createDB(self):
    conn = sqlite3.connect('sensor.db')
    cur = conn.cursor()
    cur.execute('''CREATE TABLE notified(notifieddates datetime);''')
    conn.close()


def checkIfNotifiedToday(self):
    DATE_FORMAT = "%Y-%m-%d"
    conn = sqlite3.connect('sensor.db')
    cur = conn.cursor()
    row = cur.execute(
        "SELECT DATE(MAX(notifieddates)) FROM notified").fetchone()
    recentDate = datetime.strptime(row[0], DATE_FORMAT)
    recentDate = recentDate.strftime(DATE_FORMAT)
    now = datetime.now()
    now = now.strftime(DATE_FORMAT)
    conn.close()

    if(recentDate == now):
        return 0
    else:
        return 1

def insertNotifiedDate(self):
    conn = sqlite3.connect('sensor.db')
    cur = conn.cursor()
    cur.execute('''INSERT INTO notified VALUES(DATE('now'))''')
    conn.close()