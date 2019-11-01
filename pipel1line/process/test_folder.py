#!/usr/bin/python3

import os

class Folder:

    folder="/home/tron/wildtest/woohoo"
    if not os.path.exists(folder):
        print("folder does not exist... creating...")
        os.makedirs(folder)
    else:
        print("folder exists...")

f1=Folder()
