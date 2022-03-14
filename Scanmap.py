#!/usr/bin/python3
# ScanMap - A Multi Threader Port Scanner
# A project by Anmol
# https://github.com/r0g4r

# Imports
import socket
import os
import signal
import time
import threading
import sys
import subprocess
from queue import Queue
from datetime import datetime

# Start Scanner with clear terminal
subprocess.call('cls', shell=True)

# Main Function
def main():
    socket.setdefaulttimeout(0.30)
    print_lock = threading.Lock()
    discovered_ports = []

# Welcome Banner
    print("*" * 70)
    print('''
    ███████╗ ██████╗ █████╗ ███╗   ██╗███╗   ███╗ █████╗ ██████╗ 
    ██╔════╝██╔════╝██╔══██╗████╗  ██║████╗ ████║██╔══██╗██╔══██╗
    ███████╗██║     ███████║██╔██╗ ██║██╔████╔██║███████║██████╔╝
    ╚════██║██║     ██╔══██║██║╚██╗██║██║╚██╔╝██║██╔══██║██╔═══╝ 
    ███████║╚██████╗██║  ██║██║ ╚████║██║ ╚═╝ ██║██║  ██║██║     
    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝     ╚═╝╚═╝  ╚═╝╚═╝                                                            
                                               
                            By - ANMOL(R0G4R)  
    ''')
    print("*" * 70)
    time.sleep(1)
    target = input("Enter your target IP address or URL here: ")
    error = ("Invalid Input")
    try:
        t_ip = socket.gethostbyname(target)
    except (UnboundLocalError, socket.gaierror):
        print("\n[-]Invalid format. Please use a correct IP or web address[-]\n")
        sys.exit()
    #Banner
    print("-" * 60)
    print("Scanning target "+ t_ip)
    print("Time started: "+ str(datetime.now()))
    print("-" * 60)
    t1 = datetime.now()

    def portscan(port):

       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
       
       try:
          portx = s.connect((t_ip, port))
          with print_lock:
             print("Port {} is open".format(port))
             discovered_ports.append(str(port))
          portx.close()

       except (ConnectionRefusedError, AttributeError, OSError):
          pass

    def threader():
       while True:
          worker = q.get()
          portscan(worker)
          q.task_done()
      
    q = Queue()
     
    #startTime = time.time()
     
    for x in range(200):
       t = threading.Thread(target = threader)
       t.daemon = True
       t.start()

    for worker in range(1, 65536):
       q.put(worker)

    q.join()

    t2 = datetime.now()
    total = t2 - t1
    print("Port scan completed in "+str(total))
    print("-" * 60)



if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        quit()