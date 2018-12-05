#!/usr/bin/python
#coding:utf-8

import threading
import time


def worker1(j):
    """
    thread worker function
    :return:
    """
    for i in range(len(nums)):
        nums[i] = j
    return

def worker2(j):
    """
    thread worker function
    :return:
    """
    time.sleep(0.0007345)
    for i in range(len(nums)):
        nums[(len(nums)-i-1)] = j
    return


def worker3():

    print nums
    return

nums = []

for i in range(100000):
    nums.append(0);


t1 = threading.Thread(target=worker1, args=(1, ), name="%s" % "thread-1")
name = t1.getName()
print("Thread %s starts" % name)
t1.start()

t2 = threading.Thread(target=worker2, args=(7, ), name="%s" % "thread-2")
name = t2.getName()
print("Thread %s starts" % name)
t2.start()

t3 = threading.Thread(target=worker3, name="%s" % "thread-3")
name = t3.getName()
print("Thread %s starts" % name)
t3.start()

# for i in range(100000):
#     #print i
#     nums.append(i)

#for num in nums:
	# print("%d" % num)