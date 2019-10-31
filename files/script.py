#!/usr/bin/env python3

import docker
import os, subprocess
import sys, six

###
# on local machine:
# pip3 install docker
# mkdir -p /home/hparsed
#


####################################################################
# Step 1:
# build script that will process data inside our python3 container
#


def CreateDataScript():

    str = """#!/usr/bin/python3
import time
import pandas as pd
import numpy as np
import os, subprocess
import sys


def dataframes():

    def pro(argv):
        container=sys.argv[1]

        def paths(argv):

            directory = sys.argv[2]


            class DeclareParam(object):
                def __init__(self,
                    processed_directory,
                    not_processed_directory,
                    filename,
                    filename1,
                    command_copy,
                    command_remove):

                    self.dddd = processed_directory
                    self.eeee = not_processed_directory
                    self.fi = filename
                    self.fi1 = filename1
                    self.ff = command_copy
                    self.ff1 = command_remove

            lll  = DeclareParam(directory+"edw_status=processed/", directory+"edw_status=not_processed/", "/home/cparsed/filename", "/home/cparsed/filename1", "/home/cparsed/files_to_copy", "/home/cparsed/files_to_remove")
            
            class DeclarePath:
                def __init__(self, new_dir, new_dir1):
                    self.n = new_dir
                    self.n1 = new_dir1
            d = DeclarePath("/home/cparsed/test_not_processed.txt", "/home/cparsed/test_processed.txt")



            def formula():
                def splitall(directory):
                    allparts = []
                    while 1:
                        parts = os.path.split(directory)
                        if parts[0] == directory:
                            allparts.insert(0, parts[0])
                            break
                        elif parts[1] == directory:
                            allparts.insert(0, parts[1])
                            break
                        else:
                            directory = parts[0]
                            allparts.insert(0, parts[1])
                    return allparts

                pampam = splitall(directory)
                print(pampam)

                ####################################
                # function to provide any path
                ####################################
                def bitz():

                    m = len(pampam[1:])
                    print( m )

                     #this moffo!
                    t_pam = tuple(pampam[1:])
                    print(t_pam)

                    #Wild formula..lmao!

                    s = "\/%s"
                    n=4*(m-1)

                    for i in range(n):
                        s+=s[i]


                    def commandz():
                        print(" hello %s from commandz" % (s))
                        kiki1 = "sed -e 's/%sedw_status=not_processed\///g' -e  '1i not_processed' " % (s)
                        print("hello from bitz to %s " % (kiki1))
                        jjjjj1 = kiki1 % (t_pam)
                        print("hello to  %s from commanz " % (jjjjj1))


                        def dataframez():
                            print("=================")
                            print(d.n)
                            print(d.n1)

                            time.sleep(2)
                            data = pd.read_fwf(d.n)
                            df = pd.DataFrame(data,columns=['not_processed'])

                            data1 = pd.read_fwf(d.n1)
                            df1 = pd.DataFrame(data1,columns=['processed'])

                            print ("duplicates:")
                            hue = np.intersect1d(df['not_processed'], df1['processed'])

                            print("nr of duplicates")
                            eh = hue.size
                            print(eh)

                            print("turn array into list")
                            meh = hue.tolist()

                            print(hue.size)


                            def old_commandz():


                                 def generate_commandz():
                                     kiki1 = "sed -e 's/%sedw_status=not_processed\///g'  -e  '1i not_processed' " % (s)
                                     jjjjj1 = kiki1 % (t_pam)

                                     kiki2 = "sed -e 's/%sedw_status=processed\///g'  -e  '1i processed' " % (s)
                                     jjjjj2 = kiki2 % (t_pam)

                                     cmd = "cat /home/cnotparsed/not_processed.txt | awk {'print $8'} | %s  > /home/cparsed/test_not_processed.txt"  % (jjjjj1)
                                     procp = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

                                     cmd1 = "cat /home/cnotparsed/processed.txt | awk {'print $8'} | %s  > /home/cparsed/test_processed.txt"  % (jjjjj2)
                                     procp1 = subprocess.Popen(cmd1, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

                                     print(hue.size)
                                     #def hue():
                                     #    print(hue.size)
                                     for i in range(0, hue.size):
                                         print(lll.eeee+meh[i], end=' ', file=open(lll.fi, "a"))
                                     with open(lll.fi, 'r') as copy_file:
                                         print("docker exec %s hdfs dfs -cp -f  %s %s" % (container,  copy_file.readline(), lll.dddd), file=open(lll.ff, "w"))

                                     for j in range(0, hue.size):
                                         print(lll.eeee+meh[j], end=' ', file=open(lll.fi1, "a"))
                                     with open(lll.fi, 'r') as rem_files:
                                         print("docker exec %s hdfs dfs -rm %s" % (container, rem_files.readline()), file=open(lll.ff1, "w"))


                                 generate_commandz()

                            old_commandz()
                        dataframez()

                    commandz()

                bitz()

            formula()

        paths(sys.argv[2])

    pro(sys.argv[1])

# pfew! done with inner functions

def delete_files():

    class DeclarePathRemoving():
        def __init__(self, f_del, f_del1):
            self.x = f_del
            self.x1 = f_del1

    chic = DeclarePathRemoving(
        "/home/cparsed/filename",
        "/home/cparsed/filename1"
       )
    time.sleep(2)

    print(" program terminating...  will be deleted for a new re-run: filename and filename1...")
    print(" ")
    print(" ###### Perform in order the following actions: first you COPY, then you REMOVE the files ###### ")
    os.system("rm %s" % (chic.x))
    os.system("rm %s" % (chic.x1))

    print("find the commands for copy files in file:  under /home/cparsed/files_to_copy")
    print("find the command for removing files in file:  under /home/cparsed/files_to_remove")
    print(" ")


def create_scripts():

    dirdir = "/home/cparsed/files_to_copy"
    script = "cat /home/cparsed/files_to_copy | sed -e '1i #!/bin/bash' > /home/cparsed/script_files_to_copy.sh"
    create_script = subprocess.Popen(script, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    print("find the script for copy under: /home/cparsed/script_files_to_copy.sh")


    dirdir1 = "/home/cparsed/files_to_remove"
    script1 = "cat /home/cparsed/files_to_remove | sed -e '1i #!/bin/bash' > /home/cparsed/script_files_to_remove.sh"

    create_script1 =  subprocess.Popen(script1, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)
    print("find the script for remove under:  /home/cparsed/script_files_to_remove.sh")

def main():

    print("le lel!")

if __name__ == "__main__":
    main()
    dataframes()
    delete_files()
    create_scripts()

"""

    f_f = open("/home/hscriptparse/script_2_process.py", "w")
    f_f.write(str)
    f_f.close()

def CreateNotebook():

    str1 = """{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "! ls /home/cscriptparse"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "! ./script_2_process.py <containerID> sales"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "! ./script_2_process.py <containerID> products"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
"""

    g_g = open("/home/hscriptparse/notebook2check.ipynb", "w")
    g_g.write(str1)
    g_g.close()


######################################
# create our python3 container image
# and build container
#####################################

def BuildImage():
    dockerfile = '''
    FROM ubuntu
    RUN apt-get update
    RUN apt-get install curl -y
    RUN apt-get install build-essential -y
    RUN apt-get install python3 -y
    RUN apt-get install software-properties-common -y
    RUN apt-get install python3-setuptools -y
    RUN apt-get install python3-pip -y
    RUN apt-get update
    RUN apt-get install ipython -y
    RUN pip3 install jupyter

    RUN pip3 install numpy
    RUN pip3 install pandas
    WORKDIR /home/cscriptparse
    '''

    f = six.BytesIO(dockerfile.encode('utf-8'))

    cli = docker.APIClient(base_url='unix://var/run/docker.sock')

    response = [line for line in cli.build(fileobj=f, rm=True, tag='popey:latest')]

    print(response)
    print("      ")
    print("The image is now built...")

def BuildContainer():
    print("starting to build container")
    client = docker.APIClient(base_url='unix://var/run/docker.sock')
    
    
    #####
    # mount 3 folders host:container
    #####
    container_id = client.create_container('popey',
                                      volumes=['/home/cnotparsed', '/home/cparsed', '/home/cscriptparse'], ports=[8888, 8889],
                                      host_config=client.create_host_config(binds=['/home/hnotparsed/:/home/cnotparsed',
                                                                                     '/home/hparsed/:/home/cparsed',
                                                                                     '/home/hscriptparse:/home/cscriptparse'],
                                                                             port_bindings= { 8888: 8888, 8889: None}),
                                        stdin_open=True, tty=True,
                                        command='/bin/sh',
                                        detach=True )

    client.start(container_id)

def main():
    CreateDataScript()
    CreateNotebook()
    BuildImage()
    BuildContainer()

if __name__ == "__main__":
    main()
