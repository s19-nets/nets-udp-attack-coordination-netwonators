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

r_set = set([server_socket, client_socket])
w_set = set()
e_set = set([server_socket, client_socket])

timeout = 5

state = "idle" 

while True: 
    time.sleep(random.randrange(2,5))

    readready, writeready, error = select(r_set, w_set, e_set, timeout)

    if not readready:
        count = 0
        if state == "idle": 
            msg = "marco"
            server_socket.sendto(msg.encode(), server_addr)
            sent_time = time.time()
            state = "wait" 
            print("i sent %s" % msg)
        elif state == "wait" and time.time() - sent_time >= 5: 
            msg = "marco"
            server_socket.sendto(msg.encode(), server_addr)
            count += 1
            print("Message %s was sent %d times" % (msg, count))
        else: 
            print("Something went wrong bye")
            sys.exit(1)
    else:
        for sock in readready: 
            message, port = client_socket.recvfrom(2048)
            print("I have recived %s from %s" % (message, repr(port)))

