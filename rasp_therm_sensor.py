#!/usr/bin/python

"""
	Description: Raspberry PI thermostat with a DS18B20 sensor.
	Author: Steffen Pettersen <stejp96@gmail.com>
	Dependencies: Rasperry PI python library. DS18B20 sensor.
	License: This code can be used, modified and distributed freely, 
	 as long as this note containing the original author, the source and this license, is put along with the source code.
"""

import time
import subprocess
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.OUT)
GPIO.setwarnings(False)

currentState = None
temperature = 0
degrees = 25.0

def GPIOSet(state):
	global currentState
	if state == currentState:
		return
	currentState = state
	if state:
		GPIO.output(3, GPIO.HIGH)
		print ("Set pin 3 to HIGH")
	else:
		GPIO.output(3, GPIO.LOW)
		print ("Set pin 3 to LOW")
	return

def CheckMod():
	a = subprocess.Popen('lsmod', stdout=subprocess.PIPE)
	b = subprocess.Popen(['grep', 'w1_gpio'], stdin=a.stdout, stdout=subprocess.PIPE)
	a1 = subprocess.Popen('lsmod', stdout=subprocess.PIPE)	
	c = subprocess.Popen(['grep', 'w1_therm'], stdin=a1.stdout, stdout=subprocess.PIPE)
	result_str = b.communicate()[0]	
	result_str2 = c.communicate()[0]
	if result_str.find("w1_gpio") == -1:
		subprocess.Popen('sudo modprobe w1-gpio', shell=True)
		print("Ran the command w1-gpio")
	else:
		print("Didn't load 'w1-gpio'")
	if result_str2.find("w1_therm") == -1:
		subprocess.Popen('sudo modprobe w1-therm', shell=True)
		print("Ran the command w1-therm")
	else: 
		print("Didn't load 'w1-therm'")
	return;

def GetTemp():
	global temperature
        try:
		time.sleep(2)
		tfile = open("/sys/bus/w1/devices/28-0000046d339d/w1_slave")
	except IOError:
		print("Couldn't load file")
	text = tfile.read()
	tfile.close()
	temperaturedata = text.split("\n")[1].split(" ")[9]
	temperature = float (temperaturedata[2:])
	temperature /= 1000
	return; 	
        
def Loop():
	CheckMod()
	while(True):
		GetTemp()
		print temperature
		if temperature >= degrees:
			GPIOSet(False)
		else:
			GPIOSet(True)
	return;

if __name__=="__main__":
	Loop()
