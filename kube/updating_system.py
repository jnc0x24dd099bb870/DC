#!/usr/bin/python3
import subprocess
from subprocess import STDOUT, check_call
import os
import sys


class Updates(object):
    def __init__(self, update=None):
        if update is None:
            update={}
        else:
           self.update=update
    def upd(self):
        print("\n===== Performing updates  ======\n")
        check_call(['apt', 'update'], stderr=STDOUT)

    def install(self, shell=True):
        print("\n===== Install necessary packets  ======\n")
        listofpackets = ['apt-transport-https', 'ca-certificates', 'curl', 'software-properties-common', 'python3-pip']
        for update in listofpackets:
            check_call(['apt', 'install', '-y', update], stderr=STDOUT)


