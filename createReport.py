#Generates a csv file.
#Each row contains a day's data, temperature and humidity range.
#Status OK, or BAD based on the range.
#Has to be executed manually.

import sqlite3, configFetcher, csv
from datetime import datetime, timedelta

DB_NAME = "sensor.db"
DATE_FORMAT = "%Y-%m-%d"
ONE_DAY_DELTA = timedelta(days = 1)

class Reporter:

        def generateReportString(self, recordedTempMax, recordedTempMin, recordedHumMax, recordedHumMin, maxTemp, maxHum, minTemp, minHum, currentDate):
                        """compare the values from the config file with each of the day's MIN/MAX values and
                        generate a string that is then passed on to the generateReport method. """
                
                        message=""
                        flag = "OK "
                        if(recordedTempMax>maxTemp):
                                percent = (recordedTempMax/maxTemp)*100
                                message = message+" current temperature exceeds configured temperature by " + str(percent) + "%."
                                flag = "BAD: "

                        if(recordedTempMin<minTemp):
                                percent = (recordedTempMin/minTemp)*100
                                message = message+"current temperature is"+str(percent)+ "% below configured temperature. "
                                flag = "BAD: "

                        if(recordedHumMax>maxHum):
                                percent = (recordedHumMax/maxHum)*100
                                message = message+"current humidity exceed configured humidity by " + + str(percent) + "%."
                                flag = "BAD: "

                        if(recordedHumMin<minHum):
                                percent = (recordedHumMin/minHum)*100
                                message = message+"current humidity is "+str(percent)+ "% below configured humidity. "
                                flag = "BAD: "
                        return message,flag

        
        def generateReport(self):
                connection = sqlite3.connect(DB_NAME)
                connection.row_factory = sqlite3.Row
                
                with connection:
                        cursor = connection.cursor()
                        row = cursor.execute("SELECT DATE(MIN(date)), DATE(MAX(date)) FROM sensor").fetchone()
                        startDate = datetime.strptime(row[0], DATE_FORMAT)
                        endDate = datetime.strptime(row[1], DATE_FORMAT)

                        print("Report:")
                        date = startDate

                        with open("report.csv", "w", newline="") as csvfile:
                                writer = csv.writer(csvfile)
                                while date <= endDate:
                                        row = cursor.execute(
                                                """SELECT COUNT(*), max(temperature), min(temperature), max(humidity), min(humidity) FROM sensor
                                                WHERE date >= DATE(:date) AND date < DATE(:date, '+1 day')""",
                                                { "date": date.strftime(DATE_FORMAT) }).fetchone()
                                        
                                        print(date.strftime(DATE_FORMAT) + " | Readings recorded: " + str(row[0]) + "\nMax Temperature: " + str(row[1]) + "\nMin Temperature: " + str(row[2]) + "\nMax Humidity: " + str(row[3]) + "\nMin Humidity: " + str(row[4]) + "\n" )
                                        recordedTempMax = row[1]
                                        recordedTempMin = row[2]
                                        recordedHumMax = row[3]
                                        recordedHumMin = row[4]
                                        maxTemp = configFetcher.getMaxTemperature()
                                        minTemp = configFetcher.getMinTemperature()
                                        maxHum = configFetcher.getMaxHumidity()
                                        minHum = configFetcher.getMinHumidity()
                                        currentDate=date.strftime(DATE_FORMAT)

                                        reportString, flag = self.generateReportString(recordedTempMax, recordedTempMin, recordedHumMax, recordedHumMin, maxTemp, maxHum, minTemp, minHum, currentDate)
                                        writer.writerow([currentDate,flag+reportString])
                                        date += ONE_DAY_DELTA
                connection.close()


# Execute program.
if __name__ == "__main__":
    report = Reporter()
    report.generateReport()
