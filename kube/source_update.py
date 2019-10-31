#!/usr/bin/python3

import subprocess
from subprocess import STDOUT, check_call
import os
import sys

def install():
    # I know, I know... os.system() such bad practice...
    os.system("curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -")

    os.system("add-apt-repository \"deb [arch=amd64] http://apt.kubernetes.io/ kubernetes-xenial main\"")

