import serial
import os

###need the output of ls /dev/cu.usbmodem*
#ArdunioLocation = ????

retvalue = os.system("ls /dev/cu.usbmodem*")
print retvalue


import os
p = os.popen('command',"r")
while 1:
    line = p.readline()
    if not line: break
    print line



ser = serial.Serial(ArdunioLocation, 115200)
while True:
	print ser.readline(),
