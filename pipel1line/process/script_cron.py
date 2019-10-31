#!/usr/bin/python3

import os

def cron_script():
    str_cron="""* * * * * root  /usr/bin/python3  /home/insert_some.py"""

    g_g = open("/home/wild_project/py/ha/cr0n/meh/dba-cron", "w")
    g_g.write(str_cron)
    g_g.close()
