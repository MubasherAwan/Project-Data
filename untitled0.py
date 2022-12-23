# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 09:23:37 2022

@author: iammu
"""


import socket
import threading


print_lock =threading.Lock()

def createThread(c,addr):
  print(f"new connection : {addr}")
  print(f"ThreadName : ",{threading.currentThread().getName()})
  while True:
    data = c.recv(1024)
    print('Recieved fro,m the client : ',str(data.decode('ascii')))
    if not data:
      print('Bye')
      print_lock.release()
      break
    data= 'Today we will learn About multiThreading with socket programming'
    c.send(data.encode('utf-8'))
  c.close()

def MyMain():
  host='localhost'
  port=2022
  s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  s.bind((host,port))
  print("Socket binded to port ",port)
  s.listen()
  print("Server is Listening, Waiting for incoming ")
  while True:
    c,addr=s.accept()
    print_lock.acquire()

    print('Connect to : ',addr[0]," : ",addr[1])
    print(f"threadName , before creating thread: :",{threading.currentThread().getName()})
    thread = threading.Thread(target=createThread,args=(c,addr))
    thread.start()
  s.close()


print("Calling Main Function")
MyMain()