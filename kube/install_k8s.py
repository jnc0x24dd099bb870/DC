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

class Install(object):
    def __init__(self, service=None):
        if service is None:
            service={}
        else:
            self.service=service_k8s

    def ins(self, shell=True):
        listofcomponents = ['kubelet', 'kubeadm', 'kubectl']
        for update in listofcomponents:
            check_call(['apt', 'install', '-y', update], stderr=STDOUT)

    def pip_client(self, shell=True):
        self.service='kubernetes'
        check_call(['pip3', 'install', self.service], stderr=STDOUT)
