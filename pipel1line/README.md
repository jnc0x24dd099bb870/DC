<b>Simple data flow example</b>

The data flow has 3 components:
1) ingestion - done by a containerized cronjob that retrives csv from ftp
2) storage - the containerized cronjob sends data into mysql as dataframes
3) jupyter for analysis (by accessing the stored data in mysql)

*Schema*
```
+-------+.    (retrive)
|  FTP  +<<<-------------+                         (analysis)    +-----------+
+-------+                |                     +-------------->>>+  jupyter  |
                    +----+----+                |                 +-----------+
                    | cronjob |                |
                    +----+----+                |
                         |      (store)  +-----+----+             
                         +------------>>>+   mysql  |
                                         + ---------+
                                  
```

*Build environment*

Part 1) and 2) is implemented by programs (main program: cron_main.py) under pipel1line/process and pipel1line/ftp.

The pipel1line/ftp program will allow you to run locally a small ftp server that will provide the weather_data.csv data.

Suppose my ftp script &weather_data.csv are under /home/cons:
```
root@tr0n:/home/cons# ls /home/cons
heh.py  stuff.txt weather_data.csv
````
Run script:
```
root@tr0n:/home/cons# strace ./heh.py 
execve("./heh.py", ["./heh.py"], 0x7ffea90803f0 /* 31 vars */) = 0
[....snip....]
getpid()                                = 4474
write(3, "INFO:pyftpdlib:passive ports: No"..., 35) = 35
epoll_wait(4, 
````
Check if all good:

```
root@tr0n:/home/waht# lsof -i :2121
COMMAND  PID USER   FD   TYPE  DEVICE SIZE/OFF NODE NAME
heh.py  4474 root    5u  IPv4 3035277      0t0  TCP *:iprop (LISTEN)
root@tr0n:/home/waht# 
```


From there, the pipel1ne/process does as following (just run cron_main.py)

a) creating containerized cronjob that will establish connection with ftp

b) retriving the weather_data.csv

c) storing dataframes into mysql 


For point a) you will have to run manually the command "service cron start" for the cronk container
```
root@tr0n:/home/tron/hue/DC/pipel1line/process# docker exec cronak service cron status
 * cron is not running
root@tr0n:/home/tron/hue/DC/pipel1line/process#  docker exec cronak service cron start
 * Starting periodic command scheduler cron
   ...done.
root@tr0n:/home/tron/hue/DC/pipel1line/process# docker exec cronak service cron status
 * cron is running
 ```
 For mysql container, use the official image, as per indications at <a href="https://dev.mysql.com/doc/mysql-installation-excerpt/5.5/en/docker-mysql-getting-started.html">MySQL link</a>
 
 Don't forget to grant privileges, so that you can access database/tables either from container or localhost:
``` 
GRANT ALL PRIVILEGES ON *.* TO 'root'@'localhost'  WITH GRANT OPTION;
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%'  WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

Code is a bit hardcoded from a networking side (containers' IP), path for weather_data.csv file (feel free to change it),
and MySQL passwd &dba (named "huehue")

MySQL container mysql1 is 172.17.0.2 as per code.

On MySQL side, after running the mentioned scripts
```
root@tr0n:/home/tron/wildtest/DC/pipel1line/process# docker exec mysql1 mysql -u root -pabc123 -e "use huehue; select * from hall0ween;"
mysql: [Warning] Using a password on the command line interface can be insecure.
day	temperature	windspeed	event
1/1/2017	32	6	Rain
1/2/2017	35	7	Sunny
1/3/2017	28	2	Snow
```

Jupyter is installed on local machine - just as the ftp server. (the only services on containers are mysql &cronjob).

Follow <a href="https://hostadvice.com/how-to/how-to-install-jupyter-notebook-on-ubuntu-18-04-vps-or-dedicated-server/">link</a> for installing Jupyter locally. (no code for this part)

Small test on how to access data from container:

![ScreenShot](https://raw.githubusercontent.com/jnc0x24dd099bb870/DC/master/pipel1line/data/jup.png) 


to be done: static IP for containers & port jupyter to a container

