import socket
import os
import subprocess
import pyautogui
import threading
s=socket.socket()
host="XXX.XXX.XX.X" #Host Ip address
port="XXXX" #port number 
s.connect((host,port))
def sendMsg():
	try:
		send = input(">>")
		s.send(send.encode("utf-8"))
	except Exception as e:
		sendMsg()
def recving():
	while True:
		try:
			dt = str(s.recv(1024),'utf-8')
			print(dt)
		except Exception as e:
			recving()
thr1 = threading.Thread(target=recving)
thr1.start()
# thr2 = threading.Thread(target=sendMsg)
# thr2.start()
name = input("Enter your name : ")
s.send(name.encode('utf-8'))
while True:
	sendMsg()


	
