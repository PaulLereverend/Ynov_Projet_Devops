#!/usr/bin/env python

import os
import time
import getpass
from config import *

def get_dump():
    filestamp = time.strftime('%Y-%m-%d-%I:%M')
    if (db_type == 'mariadb'):
        get_dump_mariadb(filestamp)
    else:
        print("Error")
    print("\n-- please have a the dump file in "+database+"_"+filestamp+".gz --")

def get_dump_mariadb(filestamp):
    os.popen("mysqldump -u %s -p%s -h %s -e --opt -c %s | gzip -c > /backups/%s.gz" % (user,password,host,database,database+"_"+filestamp))

if __name__=="__main__":
    get_dump()