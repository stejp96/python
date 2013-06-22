import time
import subprocess
#import RPi.GPIO as GPIO
#GPIO.setup(14, output)

'''
def GPIOFalse():
GPIO.output(14, False)
return;
'''

'''
def GPIOTrue():
GPIO.output(14, True)
return;
'''

def CheckMod():
str1 = w1-gpio
str2 = w1-therm
	a = subprocess.Popen('lsmod', stdout=subprocess.PIPE)
	b = subprocess.Popen(['grep', str1], stdin=a.stdout, stdout=subprocess.PIPE)
	c = subprocess.Popen(['grep', str2], stdin=a.stdout, stdout=subprocess.PIPE)
	result_str = b.communicate()[0]	
	result_str2 = c.communicate()[0]
	return;

def GetTemp():
        degrees = 25.0
        tfile = open("/sys/bus/w1/devices/28-0000046d339d/w1_slave")
        text = tfile.read()
        tfile.close()
        temperaturedata = text.split("\n")[1].split(" ")[9]
        temperature = float (temperaturedata[2:])
        temperature /= 1000
        #print temperature;
        return;

def RunCommands(a):
        modprobe1 = "sudo modprobe w1-gpio"
        modprobe2 = "sudo modprobe w1-therm"
	if a = 1: 
        subprocess.Popen('modprobe1', shell=True)
	elif a = 2:
        subprocess.Popen('modprobe2', shell=True)
	else: print "some error in RunCommands()"
        return;

def StartUp():
    count = 0
    while count == 0:
      print ("Starting up...")
      count +=1 
        
def Main():
	time.sleep(1)
	if result_str.find(str1) == -1:
		RunCommands(1)
	elif result_str2.find(str2) == -1:
		RunCommands(2)
	time.sleep(5)
	if temperature > degrees:
	   print temperature;
	   GPIOTrue()
	else: 
	    print("Less than 25 degrees")
	  
	

while (true):
	StartUp()
	 time.sleep(2)
        Main()
	time.sleep(2)






