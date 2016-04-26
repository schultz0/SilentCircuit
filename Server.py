import serial
import os
import platform
import glob
import sys

## This lets us know if we are running the program on a Mac or Linux Computer.
#print platform.system()
if platform.system() == 'Darwin':
    computerSystem = 'Mac'
elif platform.system() == 'Linux':
    computerSystem = 'Raspi'
else:
    computerSystem = 'Unknown'
print "I hope you are using a", computerSystem


if computerSystem == 'Mac':
    typeFile = "/dev/cu.usbmodem*"
elif computerSystem == 'Raspi':
    typeFile = "/dev/ttyAMC*"

ardunioLocation = glob.glob(typeFile)
if not ardunioLocation:
    print "I do not see an Arduino"
    sys.exit()
else:
    print "Your Arduino is at",
    print ardunioLocation[0]


ser = serial.Serial(ardunioLocation[0], 115200)
while True:
	print ser.readline(),
