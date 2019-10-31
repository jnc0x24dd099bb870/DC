#!/usr/bin/env python3

import os, subprocess

def create_folder():
    global folder
    folder="/home/tron/wildtest/woohoo"
    if not os.path.exists(folder):
        print("folder does not exist... creating...")
        os.makedirs(folder)
    else:
        print("folder exists...")

create_folder()



def dba_script():
    str="""#!/usr/bin/python3

import os
from sqlalchemy import create_engine

import pymysql
import pandas as pd

import ftpy

from ccc import User
from ccc import Passwd
from ccc import Host
from ccc import Dba


haha = "/home/weather_data.csv"
dataFrame   = pd.read_csv(haha)

print(User.name)
print(Passwd.secret)
print(Host.hostname)
print(Dba.database)

class SQL(object):
    
    def __init__(self, sqlEngine=None, dbConnection=None, table=None):
        if sqlEngine is None:
            sqlEngine={}
        else:
            self.sqlEngine=sqlEngine
        if dbConnection is None:
            dbConnection={}
        else:
            self.dbConnection=dbConnection
        if table is None:
            self.table={}
        else:
            self.table=table


    def create_table(self):
        self.table='hall0ween'
        self.sqlEngine = 'mysql+pymysql://'+User.name+':'+Passwd.secret+'@'+Host.hostname+':3306/'+Dba.database
        dbConnection = create_engine(self.sqlEngine).connect()
        return  dataFrame.to_sql(self.table, dbConnection, if_exists='append', index=False); 

if __name__ == '__main__': 
    SQL().create_table() 
"""

    h_h = open(folder+"/insert_some.py", "w")
    h_h.write(str)
    h_h.close()

