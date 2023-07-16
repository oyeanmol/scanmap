#!/usr/bin/python3
# ScanMap - A Multi Threader Port Scanner
# A project by Anmol
# https://github.com/oyeanmol

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
                            By - ANMOL  
    ''')
    print("*" * 70)
    time.sleep(1)
    target = input("Enter Target Url or IP: ")
    error = ("Invalid Input!!")
    try:
        t_ip = socket.gethostbyname(target)
    except (UnboundLocalError, socket.gaierror):
        print("\n[-]Invalid format. Please use a correct IP or web address[-]\n")
        sys.exit()
    # Banner
    print("-" * 60)
    print("Scanning target " + t_ip)
    print("Time started: " + str(datetime.now()))
    print("-" * 60)
    t1 = datetime.now()

    def portScan(port):

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
            portScan(worker)
            q.task_done()

    q = Queue()

    for x in range(200):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    for worker in range(1, 65536):
        q.put(worker)

    q.join()

    t2 = datetime.now()
    total = t2 - t1
    print("Port scan completed in "+str(total))
    print("-" * 60)
    print("-" * 60)
    print("ScanMap Recommends the following Nmap Scan: ")
    print("nmap -p {ports} -sC -sV -T4 -Pn -oA {ip} {ip}".format(ports=",".join(discovered_ports), ip=target))
    nMap = "nmap -p{ports} -sV -sC -T4 -Pn -oA {ip} {ip}".format(ports=",".join(discovered_ports), ip=target)
    t3 = datetime.now()
    total1 = t3 - t1

    # Nmap Integration

    def automate():
        choice = '0'
        while choice == '0':
            print("\nWould you like to run Nmap or quit the scan?")
            print("-" * 60)
            print("1 - Run Suggested Nmap Scan")
            print("2 - Run another ScanMap Scan")
            print("3 - Exit to terminal")

            choice = input(">> : ")

            if choice == "1":
                try:
                    print(nMap)
                    os.mkdir(target)
                    os.chdir(target)
                    os.system(nMap)

                    t3 = datetime.now()
                    total1 = t3 - t1
                    print("-" * 60)
                    print("Combined scan Complited in " + str(total1))
                    print("Press Enter to quit...")
                    input()
                except FileExistsError as f:
                    print(f)
                    exit()
            elif choice == "2":
                main()
            elif choice == "3":
                print("Exiting!!")
                sys.exit()
            else:
                print("Please make a valid Selection!")
                automate()
    automate()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\nGoodbye!")
        quit()
