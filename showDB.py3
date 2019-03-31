import datetime,time,sqlite3

conn=sqlite3.connect('sensor.db')
cur=conn.cursor()

print ("\nEntire database contents:\n")

for row in cur.execute("SELECT * FROM sensor"):
    print (row)

conn.close()