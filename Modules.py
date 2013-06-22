import subprocess

GPUTemperaturdata = 0.0
result_str = None

def GetGPUTemp():
	#Require aticonfig aka. ati gpu
	global GPUTemperaturedata
	proc = subprocess.Popen(['aticonfig --odgt | sed -n 3p | cut -c 43-47'], stdout=subprocess.PIPE, shell=True)
	GPUTemperaturedata = proc.communicate()[0]
	try:
		GPUTemperaturedata = float(GPUTemperaturedata)
	except:
		print("Invalid file data")
		return;
	print "GPU temp is", GPUTemperaturedata;
	return;

def Shutdown(minutes):
	subprocess.Popen(['shutdown -h +', minutes], shell=True)
	return;

#Use for urgency is 'low', 'normal' and 'critical'
def NotifySend(Urgency ,Message):
	#Uses notify-send to display an notification on the desktop. 
	subprocess.Popen(['notify-send', '-u' ,Urgency ,Message])
	return;

def CheckMod(Mod):
	global result_str
	a = subprocess.Popen('lsmod', stdout=subprocess.PIPE)
	b = subprocess.Popen(['grep', mod], stdin=a.stdout, stdout=subprocess.PIPE)
	result_str = b.communicate()[0]
	print result_str
	return;

