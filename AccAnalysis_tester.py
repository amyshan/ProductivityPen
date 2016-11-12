import time
import serial
import smtplib

#ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
xarray = []
yarray = []
zarray = []
xdevarray = []
ydevarray= []
zdevarray= []
count = 0;
devarray = []


x0 = 0;
y0 = 0;
z0 = 0;

xdavg = 0;
ydavg = 0;
zdavg = 0;

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
	for i in range(len(array2)):
		element = array2[i+1] - array2[i]
		devarray.append
	if count2 < len(array2):
		print(count2)
		devarray[count2] = (array2[count2+1]-array2[count2]);
		count2 += 1;
		
	return devarray;


while True:
	
	#append x,y,z raw values to data arrays in a 10 second interval
	#timeout = time.time() + 10   # time interval = 10 seconds 
	# while time.time() < timeout:# while within interval, append values
	# 	values = ser.readline()	
	# 	print(values[9])
	# 	#values = "-4 -10 50 "
	# 	numstring = ""
	# 	numarray = []
	# 	for x in values:
	# 		print(x)
	# 		if x == " ":
	# 			num = int(float(numstring))
	# 			numstring = ""
	# 			numarray.append(num)
	# 		else:
	# 			numstring += x
	# 			print(numarray)
	# 	x0 = numarray[0]
	# 	y0 = numarray[1]
	# 	z0 = numarray[2]
		
		#add init values to x y and z array
	# 	xarray[count] = x0;
	# 	yarray[count] = y0;
	# 	zarray[count] = z0;
	# 	count += 1;
	# count = 0;
	xarray = [-2,-4,6,14,4]
	yarray = [3,-1,10,8,2]
	zarray = [20,-60,2,10,5]
	#Once arrays have been filled, fill dev arrays
	#X ARRAY
	#fill xdev array & get average
	xdevarray = returndevarray(xarray);
	xdavg = get_average(xdevarray);
	# y dev array
	ydevarray = returndevarray(yarray)
	ydavg = get_average(ydevarray)
	#z array
	zdevarray = returndevarray(zarray)
	zdavg = returndevarray(zarray)
	print(xdavg)
	print(ydavg)
	print(zdavg)



	

