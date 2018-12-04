#!/usr/bin/python
#coding:utf-8

import threading
import time
 
def worker(num):
    """
    thread worker function
    :return:
    """
    time.sleep(0.01)
    print("The num is  %d" % num)
    return
 
for i in range(20):
    t = threading.Thread(target=worker, args=(i,), name="t.%d" % i)
    name = t.getName()
    print("Thread %s starts" % name)
    t.start()