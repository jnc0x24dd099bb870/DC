#!/usr/bin/python3

import docker
import os, subprocess
import sys, six

from script_dba import dba_script
from script_ftp import ftp_script
from script_cron import cron_script
from script_cred import cred_script


def BuildImage():
    dockerfile = '''
    FROM ubuntu:16.04
    RUN touch /var/log/cron.log
    RUN apt-get update
    RUN apt-get install curl -y
    RUN apt-get install build-essential -y
    RUN apt-get install python3 -y
    RUN apt-get install software-properties-common -y
    RUN apt-get install python3-setuptools -y
    RUN apt-get install python3-pip -y
    RUN apt-get update
    RUN pip3 install pymysql
    RUN pip3 install mysql-connector-python
    RUN pip3 install sqlalchemy
    RUN pip3 install pandas
    RUN apt-get -y install cron
    CMD cron && tail -f /var/log/cron.log 
    '''

    f = six.BytesIO(dockerfile.encode('utf-8'))

    cli = docker.APIClient(base_url='unix://var/run/docker.sock')

    response = [line for line in cli.build(fileobj=f, rm=True, tag='croney:latest')]

    print(response)
    print("      ")
    print("The Cron image is now built...")

def CreateContainerCron():
    print("starting to build container")
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    
    container_id = client.create_container('croney', name='cronak', ports=[2121, 2122],
                                        stdin_open=True, tty=True,
                                        host_config=client.create_host_config(port_bindings= { 2121: 2122}),
                                        command='/bin/sh',
                                        detach=True )

    client.start(container_id)

def moveFiles():
    os.system("docker cp /home/wild_project/py/ha/cr0n/meh/dba-cron cronak:/etc/cron.d/")
    os.system("docker exec cronak chmod 0644 /etc/cron.d/dba-cron")
    os.system("docker cp /home/wild_project/py/ha/cr0n/meh/ftpy.py cronak:/home")
    os.system("docker cp /home/wild_project/py/ha/cr0n/meh/insert_some.py cronak:/home")
    os.system("docker cp /home/wild_project/py/ha/cr0n/meh/ccc.py cronak:/home")
    os.system("docker exec cronak chown +x /home/insert_some.py")
              

def main():
   ftp_script()
   cron_script()
   cred_script()
   BuildImage()
   CreateContainerCron()
   dba_script()
   moveFiles()


if __name__ == "__main__":
    main()
