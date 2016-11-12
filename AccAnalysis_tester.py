import time
import serial
import smtplib

ser = serial.Serial('/dev/cu.usbmodem621', 9600)
xarray = []
yarray = []
zarray = []
xdevarray = []
ydevarray= []
zdevarray= []
count = 0;
devarray = []

prodtime = 0;
nulltime = 0;

x0 = 0;
y0 = 0;
z0 = 0;

xdavg = 0;
ydavg = 0;
zdavg = 0;

xwritemin = 0;
xwritemax = 0;
ywritemin = 0;
ywritemax = 0;
zwritemin = 0;
zwritemax = 0;


def get_average(array1):
	averagecounter = 0;
	sum = 0;
	average = 0;
	for x in array1:
		sum = sum + x;

	average = sum/len(array1)
	return average
def returndevarray(array2):
	count2 = 0;
	element = 0;
	#devarray[len(array2)-1];
	for i in range(len(array2)-1):
		element = (array2[i+1] - array2[i])
		devarray.append(element)

	return devarray;


while True:

	#append x,y,z raw values to data arrays in a 10 second interval
	timeout = time.time() + 10   # time interval = 10 seconds
	while time.time() < timeout:# while within interval, append values
		values = ser.readline()
		#values = '-3 0 60'
		print("values:")
		print(values)
		numstring = ""
		numarray = []
		for x in values:
			print(x)
			if x == " ":
				print(numstring)
				print(numarray)
				num = int(float(numstring))
				numstring = ""
				numarray.append(num)
			else:
			#if x == "0"or"1"or"2"or"3"or"4"or"5"or"6"or"7"or"8"or"9":
				numstring += x
		num = int(float(numstring))
		numstring = ""
		numarray.append(num)
		print(numarray)
		x0 = numarray[0]
		y0 = numarray[1]
		z0 = numarray[2]

		#add init values to x y and z array
		xarray[count] = x0;
		yarray[count] = y0;
		zarray[count] = z0;
		count += 1;
	count = 0;

# xarray = [-2,-4,6,14,4]
# yarray = [3,-1,10,8,2]
# zarray = [100,-60,2,10,5]
	#Once arrays have been filled, fill dev arrays
	#X ARRAY
	#fill xdev array & get average
xdevarray = returndevarray(xarray);
for x in xdevarray:
	print(x)
xdavg = get_average(xdevarray);
	# y dev array
ydevarray = returndevarray(yarray)
ydavg = get_average(ydevarray)
	#z array
zdevarray = returndevarray(zarray)
zdavg = get_average(zdevarray)
print(xdavg)
print(ydavg)
print(zdavg)

#Case 1: Writing - x: 5 to 15, y: 0 to 15, z: 5 to 15
#Case 2: Still - x: 0 to 5, y: 0 to 5, z: 0 to 5
#Case 3: Fidgeting - x: 15+, y: 15+ ,z: 15+

#Case 2 - Still
if xdavg > 5 and xdavg < 15 and ydavg > 0 and ydavg < 15 and zdavg > 5 and zdavg < 15 :
	nulltime += 10
#Case 1 - Writing
if xdavg > 5 and xdavg < 15 and ydavg > 0 and ydavg < 15 and zdavg > 5 and zdavg < 15:
	prodtime += 10
#Case 3 - Fidgeting
if ydavg > 15 and (xdavg > 15 or ydavg > 15):
	nulltime += 10
print(prodtime)
print(nulltime)
