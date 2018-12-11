#!/bin/python3

import numpy as np

input = open("4.sorted.in","r")
inputContents = input.readlines()

currentGuard = -1
sleepArrays = {}
asleepAt = -1

for event in inputContents:
    a = event.split("] ")
    b = a[0].split(" ")
    c = b[0].split("-")
    d = b[1].split(":")
    datetimestamp = {
        "month" : int(c[1]),
        "day"   : int(c[2]),
        "hour"  : int(d[0]),
        "min"   : int(d[1])
    }

    if a[1][:5] == "Guard":
        currentGuard = int(a[1].split(" ")[1][1:])
        asleepAt = -1
        if currentGuard not in sleepArrays:
            sleepArrays[currentGuard] = np.zeros(60, dtype=int)
    elif a[1].strip() == "falls asleep":
        asleepAt = datetimestamp["min"]
    elif a[1].strip() == "wakes up":
        temp = np.zeros(60, dtype=int)
        np.put(temp, list(range(asleepAt, datetimestamp["min"])), 1)
        sleepArrays[currentGuard] = sleepArrays[currentGuard] + temp
        asleepAt = -1

mostsleepy = 0
mostsleepymins = 0
for guard in sleepArrays:
        ttmins = np.sum(sleepArrays[guard])
        if ttmins > mostsleepymins:
            mostsleepy = guard
            mostsleepymins = ttmins

mostsleepyminute = np.argmax(sleepArrays[mostsleepy])

print("Most sleep is Guard #{}, with {} mins asleep\nEasiest Target = {} mins after mn\nAnswer: {}".format(mostsleepy, mostsleepymins, mostsleepyminute ,mostsleepy * mostsleepyminute))

"""
    if asleep == True:
        print("Guard is already asleep?")
    if asleep == False:
        print("Guard is already awake?")
"""
