#Generates a csv file.
#Each row contains a day's data, temperature and humidity range.
#Status OK, or BAD based on the range.
#Has to be executed manually.

import sqlite3
from datetime import datetime, timedelta

DB_NAME = "sensehat.db"
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
                WHERE timestamp >= DATE(:date) AND timestamp < DATE(:date, '+1 day')""",
                { "date": date.strftime(DATE_FORMAT) }).fetchone()
            
            print(date.strftime(DATE_FORMAT) + " | Readings recorded: " + str(row[0]) + "Max Temperature: " + str(row[1]))
            
            date += ONE_DAY_DELTA
    connection.close()

# Execute program.
if __name__ == "__main__":
    main()
