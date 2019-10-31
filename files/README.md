
<b> Implemented steps when running python3 program </b>

1) creating a Dockerfile
2) creating an image
3) creating a container with Jupyter 
4) creating a script for finding duplicates (that will exist inside the container), by comparing
   processed and not_processed files (given any path)

<p>This environment expects the files (that must be compared for duplicates) to be put under  /home/hnotparsed.
From there (because of the mount binding), all data can be accessed and processed inside container, /home/cnotparsed, 
with script_2_process.py. 
Processed data with script_2_process.py will be put under /home/cparsed. 
Once processed, it can be immediately accessed from /home/hparsed.</p>

Processed data example:

```
 from :
-rwxrwx--x+  3 hive hive      24887 2019-07-19 12:29 /data/datalake/example/edw_status=not_processed/FINAL_201907191100.csv
to 
 FINAL_201907191100.csv
```

<p>As already mentioned, this is not hardcoded and <b>  any kind of length path can be provided </b> 
(up until edw_status=not_processed/processed). This is handled by the created script script_2_process.py 
(which will be run inside the container for comparing not_processed and processed files)</p>



<i> Mount binding (cparse-hparse)</i>

On host's side (after running script, folders /home/{hscriptparse,hnotparsed,hparsed} are created)

```
root@tr0n:/home# tree /home/hscriptparse/
/home/hscriptparse/
├── notebook2check.ipynb
└── script_2_process.py

0 directories, 2 files
root@tr0n:/home# tree /home/hnotparsed
/home/hnotparsed

0 directories, 0 files
root@tr0n:/home#  tree /home/hparsed
/home/hparsed

0 directories, 0 files
```

On container's side (during program's running, folders /home/{cscriptparse,cnotparsed,cparsed} are created)
```
root@323449e2c8:/home/cscriptparse# tree /home
/home
|-- cnotparsed
|-- cparsed
`-- cscriptparse
    |-- notebook2check.ipynb
    `-- script_2_process.py

3 directories, 2 files
```

<p>Added Jupyter service inside container, 
in case you want to perform any further analysis on the files. It comes shipped with a notebook, and a small example,
on how to run the script for finding duplicates.</p>
