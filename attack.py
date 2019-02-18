#! /usr/bin/env python3

import sys, re
import time, os
import random 
from select import select
from socket import *

pid = os.getpid()

server_addr = ("", 50010)
listen_addr = ("", 50000)


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
            listen_addr = (addr, int(port))
        elif sw == "-s": 
            addr, port = re.split(":", args[0]); del args[0]
            server_addr = (addr, int(port))
        else: 
            print("Unexpected argument!")
            usage()
except: 
    usage()

server_socket = socket(AF_INET, SOCK_DGRAM)

client_socket = socket(AF_INET, SOCK_DGRAM)
client_socket.bind(listen_addr)


