<b>Simple data flow example</b>

The data flow has 3 components:
1) ingestion - done by a containerized cronjob that retrives csv from ftp
2) storage - the containerized cronjob sends data into mysql as dataframes
3) jupyter for analysis (by accessing the stored data in mysql)

*Schema*
```
+-------+.    (retrive)
|  FTP  +<<<-------------+                         analysis      +-----------+
+-------+                |                     +-------------->>>+  jupyter  |
                    +----+----+                |                 +-----------+
                    | cronjob |                |
                    +----+----+                |
                         |      (store)  +-----+----+             
                         +------------>>>+   mysql  |
                                         + ---------+
                                  
```
