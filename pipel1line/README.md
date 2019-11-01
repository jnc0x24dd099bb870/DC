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


From there, the pipel1ne/process does as following:

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
