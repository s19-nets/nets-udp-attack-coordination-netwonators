#! /usr/bin/env python3

import sys, re
import time, os

from socket import *
pid = os.getpid()

listen_addr = ("", 50000)
send_addr = ("", 50010)


def usage(): 
    print("""Usage: %s \n
            Options                        Default     Description
            [-l host:port]                   50000     Listen port number
            [-s host:port]                   50010     Send message to port number
            """ % sys.argv[1])
    sys.exit(1)

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
            usage()
#time.sleep(1)                        # sleep for 1 second


