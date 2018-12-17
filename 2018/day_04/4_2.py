#!/usr/bin/env python3

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

idxarray = []
summary = []

for guard in sleepArrays:
    summary.append(sleepArrays[guard])
    idxarray.append(guard)
summary = np.stack(summary, axis=0)

guardMostSleepy = idxarray[int(np.argmax(summary)/60)]
guardMostSleepyAt = np.argmax(summary)%60
print(guardMostSleepy, guardMostSleepyAt, guardMostSleepy * guardMostSleepyAt)
