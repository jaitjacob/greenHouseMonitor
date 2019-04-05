#Generates a csv file.
#Each row contains a day's data, temperature and humidity range.
#Status OK, or BAD based on the range.
#Has to be executed manually.

import sqlite3, configFetcher, csv
from datetime import datetime, timedelta

DB_NAME = "sensor.db"
DATE_FORMAT = "%Y-%m-%d"
ONE_DAY_DELTA = timedelta(days = 1)

# Main function.
def main():
    connection = sqlite3.connect(DB_NAME)
    connection.row_factory = sqlite3.Row
    with connection:
        cursor = connection.cursor()

        row = cursor.execute("SELECT DATE(MIN(date)), DATE(MAX(date)) FROM sensor").fetchone()
        startDate = datetime.strptime(row[0], DATE_FORMAT)
        endDate = datetime.strptime(row[1], DATE_FORMAT)

        print("Dates:")
        date = startDate
        while date <= endDate:
            row = cursor.execute(
                """SELECT COUNT(*), max(temperature), min(temperature), max(humidity), min(humidity) FROM sensor
                WHERE date >= DATE(:date) AND date < DATE(:date, '+1 day')""",
                { "date": date.strftime(DATE_FORMAT) }).fetchone()
            
            print(date.strftime(DATE_FORMAT) + " | Readings recorded: " + str(row[0]) + "\nMax Temperature: " + str(row[1]) + "\nMin Temperature: " + str(row[2]) + "\nMax Humidity: " + str(row[3]) + "\nMin Humidity: " + str(row[4]) )
            recordedTempMax = row[1]
            recordedTempMin = row[2]
            recordedHumMax = row[3]
            recordedHumMin = row[4]
            maxTemp = configFetcher.getMaxTemperature()
            minTemp = configFetcher.getMinTemperature()
            maxHum = configFetcher.getMaxHumidity()
            minHum = configFetcher.getMinHumidity()
            
            currentDate=date.strftime(DATE_FORMAT)

            if(recordedTempMax>maxTemp):
                percent = (recordedTempMax/maxTemp)*100
                message = " current temperature exceeds configured temperature by." + str(percent) + "%."

            if(recordedTempMin<minTemp):
                message = message+"current temperature is below configured temperature. "

            if(recordedHumMax>maxHum):
                message = message+"current humidity exceed configured humidity. "

            if(recordedHumMin<minHum):
                message = message+"current humidity is below configured humidity. "

            date += ONE_DAY_DELTA

            with open("report.csv", "w", newline="") as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([currentDate,message])



    connection.close()

# Execute program.
if __name__ == "__main__":
    main()
