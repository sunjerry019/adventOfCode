#!/usr/bin/env python3

# WARNING: There seems to be a edgecase where using samuel_7.in and zhiayang_7.in produces a answer that is 1 (one) tick more

import numpy as np

input = open("7.in","r")
inputContents = input.readlines()
dependencies = {}
stepsCompleted = {}
steps = []
workers = 5
workingOn = [""] * workers
workStarted = [-1] * workers
zeit = 0

for instruction in inputContents:
    a = instruction.split(" must be finished before step ")
    b = [a[0][-1], a[1][0]]
    if b[0] not in dependencies:
        dependencies[b[0]] = dict()
    if b[1] not in dependencies:
        dependencies[b[1]] = dict()
    dependencies[b[1]][b[0]] = 1

for stp in dependencies:
    print("{}: {}".format(stp, list(dependencies[stp].keys())))
print("")

def dependenciesFulfilled(key):
    df = 0
    for dependency in dependencies[key]:
        if dependency in stepsCompleted:
            df += 1
    if df == len(dependencies[key].keys()):
        return True
    return False

while True:
    #print("\033[2J", end="")
    print("t = {}, Current Steps = {}".format(zeit, "".join(steps)))
    outputLength = ["{:>4}"] * workers
    outputString = "{:<14} = [" + " ".join(outputLength) +  "]"
    print(outputString.format("WorkingOn", *workingOn))
    print(outputString.format("WorkingStarted", *[str(w) for w in workStarted]))
    for id in range(workers):
        if workStarted[id] > -1:
            if zeit == workStarted[id] + (ord(workingOn[id]) - 4):
                stepsCompleted[workingOn[id]] = 1
                steps.append(workingOn[id])
                workingOn[id] = ""
                workStarted[id] = -1

                stepsAvailable = []
                for step in dependencies:
                    if (len(dependencies[step].keys()) == 0 or dependenciesFulfilled(step)) and step not in stepsCompleted and step not in workingOn:
                        stepsAvailable.append(step)
                if len(stepsAvailable) > 0:
                    stepToDo = min(stepsAvailable)
                else:
                    stepToDo = False
                print("Worker {} = stepsAvailable = {}".format(id, stepsAvailable))
                if stepToDo:
                    workingOn[id] = stepToDo
                    workStarted[id] = zeit
        else:
            stepsAvailable = []
            for step in dependencies:
                if (len(dependencies[step].keys()) == 0 or dependenciesFulfilled(step)) and step not in stepsCompleted and step not in workingOn:
                    stepsAvailable.append(step)
            if len(stepsAvailable) > 0:
                stepToDo = min(stepsAvailable)
            else:
                stepToDo = False
            print("Worker {} = stepsAvailable = {}".format(id, stepsAvailable))
            if stepToDo:
                workingOn[id] = stepToDo
                workStarted[id] = zeit

    if len(stepsCompleted.keys()) == len(dependencies.keys()):
        print("\n=> t = {}, Final Steps = {}".format(zeit, "".join(steps)))
        break;

    #print("\033[0;0f", end="")
    print("")
    zeit += 1

    if(zeit > 3000):
        break;
