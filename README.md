# ScanMap
### A fast Multi-threaded Python Port Scanner with Nmap integration feature.

ScanMap is a script written in Python3 that allows multi-threading port scanning. The program is interactive and simply requires you to run it to begin. Once started, you will be asked to input an IP address or a FQDN as ScanMap does resolves hostnames. A full port scan take a little as 15 seconds, but as max should take less that 1 minute 30 seconds depending on your internet connection.

## Requirements
Python3 must be installed on your system in order to function pip3 for installation vai PyPi repository

## Installation
### Install via Git
`git clone https://github.com/oyeanmol/scanmap.git`

You can ass ScanMap to run from any directory by adding a symbolic link:
### For Linux
`sudo ln -s $(pwd)/scanmap.py /usr/local/bin/scanmap`
