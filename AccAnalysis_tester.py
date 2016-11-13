import time
import serial
import smtplib

ser = serial.Serial('/dev/cu.usbmodem621', 9600)

prodtime = 0;
nulltime = 0;
stilltime = 0;

x0 = 0;
y0 = 0;
z0 = 0;

def get_average(array1):
	averagecounter = 0;
	sum = 0;
	average = 0;
	for x in array1:
		sum = sum + x;
	average = sum/float(len(array1))
	return average

while True:
	#initialize variables
	xarray = []
	yarray = []
	zarray = []
	xdevarray = []
	ydevarray= []
	zdevarray= []
	count = 0;
	devarray = []
	xdavg = 0;
	ydavg = 0;
	zdavg = 0;

	#append x,y,z raw values to data arrays in a 10 second interval
	timein = time.time()   # time interval = 10 seconds

	#while time.time() < timeout:# while within interval, append values
	while count < 10:
		serialvalues = ser.readline()
		#values = serialvalues
		values = "".join([chr(c) for c in serialvalues])
		#print(values)
		numstring = ""
		numarray = []
		for x in values:
			#print(x)
			if x == " ":
				num = float(numstring)
				#print(num)
				numstring = ""
				numarray.append(num)
			else:
				numstring += x

		num = float(numstring);
		numstring = ""
		numarray.append(num)

		x0 = numarray[0]
		y0 = numarray[1]
		z0 = numarray[2]

		#add init values to x y and z array
		xarray.append(x0);
		yarray.append(y0);
		zarray.append(z0);

		if count > 0:
			xdevarray.append(xarray[len(xarray)-2] - xarray[(len(xarray)-1)])
			ydevarray.append(yarray[len(yarray)-2] - yarray[len(yarray)-1])
			zdevarray.append(zarray[len(zarray)-2] - zarray[len(zarray)-1])

		count = count + 1
		#print("count:")
		#print(count)

	xdavg = abs(float(get_average(xdevarray)))
	ydavg = abs(float(get_average(ydevarray)))
	zdavg = abs(float(get_average(zdevarray)))

	print("X avg:")
	print(xdavg)
	print("Y avg:")
	print(ydavg)
	print("Z avg:")
	print(zdavg)

	timeout = time.time()
	timeelapsed = timeout - timein
	print("time elapsed:")
	print(timeelapsed)
#Case 1: Still - x: 0 to 5, y: 0 to 5, z: 0 to 5
#Case 2: Writing - x: 5 to 15, y: 0 to 15, z: 5 to 15
#Case 3: Fidgeting - x: 15+, y: 15+ ,z: 15+

	#Case 1 - Still
	if xdavg < 0.2 and ydavg < 0.2 and zdavg < 0.2:
		nulltime += timeelapsed
		stilltime += timeelapsed
	#Case 2 - Writing
	if xdavg > 0.2 and xdavg < 1.4 and ydavg > 0.2 and ydavg < 1.4 and zdavg > 0.2 and zdavg < 1.4:
		prodtime += timeelapsed
		stilltime = 0
	#Case 3 - Fidgeting
	if ydavg > 1.4 or (xdavg > 1.4 or ydavg > 1.4):
		nulltime += timeelapsed
		stilltime = 0
	print("stilltime:")
	print(stilltime)
	print("prodtime")
	print(prodtime)
	print("nulltime:")
	print(nulltime) #that's total nulltime so far


	if stilltime > 5:
		stilltime = 0
		print("YOU STILL SON")
		time.sleep(2)
		print ("Sending Serial data")
		msg = "You still son"
		bytesw = str.encode(msg)
		ser.write(bytesw)

