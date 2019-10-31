#!/usr/bin/python3

import os

def create_folder():
    global folder
    folder="/home/tron/wildtest/woohoo"
    if not os.path.exists(folder):
        print("folder does not exist... creating...")
        os.makedirs(folder)
    else:
        print("folder exists...")

create_folder()

def cred_script():

    str="""#!/usr/bin/python3
import os
import sys


class User:
    name='root'
u1=User()
#print(u1.name)

class Passwd:
    secret='abc123'
p1=Passwd()

class Host:
    hostname="172.17.0.2"
h1=Host()

class Dba:
    database="huehue"
d1=Dba()

"""

    m_m = open(folder+"/ccc.py", "w")
    m_m.write(str)
    m_m.close()
