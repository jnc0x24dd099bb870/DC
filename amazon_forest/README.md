







Check some details:
```
root@tr0n:/home/test_py# more pair.py 
import boto3
import json

ec2 = boto3.client('ec2')
keyz = ec2.describe_key_pairs()
wanted_value = keyz['KeyPairs'][1]['KeyName']
print(wanted_value)
root@tr0n:/home/test_py# 
root@tr0n:/home/test_py# python3 pair.py
kwaie_test
root@tr0n:/home/test_py# 
```
