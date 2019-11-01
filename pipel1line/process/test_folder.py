#!/usr/bin/python3

import os


class Folder:
    folder="/home/tron/wildtest/woohoo" # do not to change this accordingly
f1=Folder()

def create_folder():
    if not os.path.exists(f1.folder):
        print("folder does not exist... creating...")
        os.makedirs(f1)
    else:
        print("folder exists...")
