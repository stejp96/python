#!/usr/bin/python

"""
  Description: Getting temperatures for CPU and GPU to keep your computer from overheating. (Only ati GPU's at this point).
  Author: Steffen Pettersen <stejp96@gmail.com>
  Dependecies: lm-sensors for CPU temp. aticonfig for GPU temp.
  Lisence: This code can be used, modefied and distributed freely, as long as this note containing the original author, the source and this license, is put along with the source code.
"""

import time
import subprocess

MessageHigh = "Temperatures reaching high levels."
MessageCritical = "Temperatures has reached critical level. Shutdown initiated in 1 minute"
#MessageNormal = "Temperatures is at a normal level"
UrgencyLow = "low"
UrgencyNormal = "Normal"
UrgencyCritical = "Critical"
CPUTemperaturedata = 0.0
GPUTemperaturedata = 0.0 

def Shutdown():
	subprocess.Popen(['shutdown -h +1',], shell=True)
	return;

def GetGPUTemp():
	global GPUTemperaturedata
	proc = subprocess.Popen(['aticonfig --odgt | sed -n 3p | cut -c 43-47'], stdout=subprocess.PIPE, shell=True)
	GPUTemperaturedata = proc.communicate()[0]
	GPUTemperaturedata = float(GPUTemperaturedata)
	print "GPU temp is", GPUTemperaturedata;
	return;

def SendMessage(urgency ,message):
	subprocess.Popen(['notify-send', '-u' ,urgency ,message])
	return;

def GetCPUTemp():
	global CPUTemperaturedata
	try:
		tfile = open("/sys/class/hwmon/hwmon0/device/temp2_input")
	except IOError:
			print("Couldn't load file")
			return;
	CPUTemperaturedata = tfile.read()
	tfile.close()
	CPUTemperaturedata = float(CPUTemperaturedata)
	CPUTemperaturedata /=1000
	print "CPU temp is", CPUTemperaturedata;
	return;

def Main():
	while True:
		time.sleep(60)
		GetGPUTemp()
		GetCPUTemp()
		if CPUTemperaturedata >= 30.0 and CPUTemperaturedata <= 60.0 or GPUTemperaturedata >= 30.0 and GPUTemperaturedata <= 60.0:
			#SendMessage(UrgencyLow, MessageNormal)
		elif CPUTemperaturedata >= 61.0 and CPUTemperaturedata <= 80.0 or GPUTemperaturedata >= 86.0 and GPUTemperaturedata <= 80.0:
			SendMessage(UrgencyNormal, MessageHigh)
		elif CPUTemperaturedata >= 81.0 and CPUTemperaturedata <= 90.0 or GPUTemperaturedata >= 81.0 and GPUTemperaturedata <= 90.0:
			SendMessage(UrgencyCritical, MessageCritical)
			Shutdown() 
			
if __name__=="__main__":
		Main()
