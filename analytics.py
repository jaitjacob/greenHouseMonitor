import sqlite3
import leather
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from dateutil import parser
from matplotlib import style

# Connect to SQLite datbase
conn = sqlite3.connect('sensor.db')
cursor = conn.cursor()

def read_from_db():
	cursor.execute('SELECT * FROM sensor')
	data = cursor.fetchall()
	print(data)
	for row in data:
		print(row)


def graph_data_1():
	cursor.execute('SELECT * FROM sensor')
	data = cursor.fetchall()

	# Get current size
	fig_size = plt.rcParams["figure.figsize"]

	# Set figure width to 9 and height to 15
	fig_size[0] = 12
	fig_size[1] = 9

	font = {'family' : 'normal',
		'size' : 10}

	matplotlib.rc('font', **font)
	plt.rcParams["figure.figsize"] = fig_size

	x = []
	y = []

	for row in data:
		x.append(row[0])
		y.append(row[1])

	fig = plt.figure()
	plt.xlabel('Timestamps')
	plt.ylabel('Temperature')
	plt.title('Scatter plot - Temperature data')
	plt.clf()
	plt.scatter(x,y)
	plt.plot(x,y)
	plt.draw()
	plt.show()
	print ("Graph generated!")
	fig.autofmt_xdate()
	fig.savefig('graph1.png')

read_from_db()
graph_data_1()

cursor.close()
conn.close()



