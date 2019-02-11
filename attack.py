#! /usr/bin/env python3

import sys, re
import time, os

from socket import *
pid = os.getpid()

listen_addr = ("", 50000)
send_addr = ("", 50010)


def usage(): 
    print("Usage: %s -l <host:port> -s <host:port>" % sys.argv[1])
    sys.exit(1)

# argument processing
try: 
    args = sys.argv[1:]
    while args: 
        sw = args[0]; del args[0]
        if sw == "-l": 
            addr, port = re.split(":",args[0]); del args[0]
            listen_addr = (addr, port)
        elif sw == "-s": 
            addr, port = re.split(":", args[0]); del args[0]
            send_addr = (addr, port)
        else: 
            print("Unexpected argument!")
            usage()

#time.sleep(1)                        # sleep for 1 second
send_socket = scoket(AF_INET, SOCK_DGRAM) # send messages socket (Client socket)

listen_socket = socket(AF_INET, SOCK_DGRAM) # listening for incoming messages socket (Server socket)
listen_socket.bind(listen_addr) #bind
""" CSMA/CD implementation: 
     
"""

