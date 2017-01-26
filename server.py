#!/usr/bin/python

import socket,time
from termcolor import cprint

try:
 cprint("[+]Server started at : {0}".format(time.ctime()),"yellow")
 sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 sock.bind(("127.0.0.1",3333))
 sock.listen(5)
 cprint("[+]Waiting for incoming connections ..","yellow")
except:
 cprint("[!]Error happend with sockets ..","red")
                                             #filename = "KeyLog{0}.txt".format(time.ctime())
                                             #f = open(filename,"w")
while 1:
 (cs , address) = sock.accept()
 fname = address[0]
 cprint("[+]Connection from address : {0}".format(address[0]),"green")
 cprint("[+]Receiving data ..")
 while 1:
  cmd = raw_input("Command : >> ")
  cs.send(cmd)
  print cs.recv(1024) 
 #f.write(cs.recv(1024))

