#!/usr/bin/python3

import os

from test_folder import Folder

def cron_script():
    str_cron="""* * * * * root  /usr/bin/python3  /home/insert_some.py"""

    g_g = open(Folder.folder+"/dba-cron", "w")
    g_g.write(str_cron)
    g_g.close()
