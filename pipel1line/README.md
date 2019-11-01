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

Part 1) and 2) is implemented by programs (main program: cron_main.py) under pipel1line/process
a) creating containerized cronjob that will establish connection with ftp
b) retriving the weather_data.csv
c) storing dataframes into mysql

For point a) you will have to run manually the command "service cron start" for the cronk container

root@tr0n:/home/tron/hue/DC/pipel1line/process# docker exec cronak service cron status
 * cron is not running
root@tr0n:/home/tron/hue/DC/pipel1line/process#  docker exec cronak service cron start
 * Starting periodic command scheduler cron
   ...done.
root@tr0n:/home/tron/hue/DC/pipel1line/process# docker exec cronak service cron status
 * cron is running
 
 
