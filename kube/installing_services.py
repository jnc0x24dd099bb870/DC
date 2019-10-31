#!/usr/bin/python3

import subprocess
from subprocess import STDOUT, check_call
import os
import sys

class Services(object):
    def __init(self, service_docker, service_nfs):
        self.service_docker=service_docker
        self.service_nfs = service_nfs

    def docker_installing(self, shell=True):
        self.service_docker='docker.io'
        check_call(['apt', 'install', '-y', self.service_docker], stderr=STDOUT)

    def nfs_installing(self, shell=True):
        self.service_nfs = 'nfs-common'

        check_call(['apt', 'install', '-y', self.service_nfs], stderr=STDOUT)
