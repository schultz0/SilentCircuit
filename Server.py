import serial
import os
import platform


## This lets us know if we are running the program on a Mac or Linux Computer.
#print platform.system()
if platform.system() == 'Darwin':
    computerSystem = 'Mac'
elif platform.system() == 'Linux':
    computerSystem = 'Raspi'
else:
    computerSystem = 'Unknown'
print "I hope you are using a ", computerSystem


if computerSystem == 'Mac':
    command = "ls /dev/cu.usbmodem*"
elif computerSystem == 'Raspi':
    command = "ls /dev/ttyAMC*"

p = os.popen(command)
location = p.read()

print location


#ser = serial.Serial(ArdunioLocation, 115200)
#while True:
#	print ser.readline(),
