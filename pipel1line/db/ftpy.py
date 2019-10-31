#!/usr/bin/python3
import ftplib
from ftplib import FTP
from pathlib import Path
import os

ftp = FTP()
ftp.connect('172.17.0.1', 2121)
ftp.login('user', '12345')
ftp.pwd()
#ftp.retrlines('LIST')

ftp.cwd('/')

#filenames = ftp.nlst()

def getFile(ftp, filename):
    try:
        ftp.retrbinary("RETR " + filename ,open(filename, 'wb').write)
    except: 
        print("perror")

getFile(ftp, 'weather_data.csv')

ftp.quit()

os.system("cp /root/weather_data.csv /home/")
