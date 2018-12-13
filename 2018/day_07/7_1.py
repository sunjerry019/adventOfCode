#!/bin/python3

import numpy as np

input = open("7.in","r")
inputContents = input.readlines()
dependencies = {}
stepsCompleted = {}
steps = []

for instruction in inputContents:
    a = instruction.split(" must be finished before step ")
    b = [a[0][-1], a[1][0]]
    if b[0] not in dependencies:
        dependencies[b[0]] = dict()
    if b[1] not in dependencies:
        dependencies[b[1]] = dict()
    dependencies[b[1]][b[0]] = 1

# print(dependencies)

def dependenciesFulfilled(key):
    df = 0
    for dependency in dependencies[key]:
        if dependency in stepsCompleted:
            df += 1
    if df == len(dependencies[key].keys()):
        return True
    return False

while True:
    stepsAvailable = []
    for step in dependencies:
        if (len(dependencies[step].keys()) == 0 or dependenciesFulfilled(step)) and step not in stepsCompleted:
            stepsAvailable.append(step)
    stepToDo = min(stepsAvailable)
    # print("Doing Step {} from {}".format(stepToDo, stepsAvailable))
    stepsCompleted[stepToDo] = 1
    # print(stepsCompleted)
    steps.append(stepToDo)
    if len(stepsCompleted.keys()) == len(dependencies.keys()):
        print("".join(steps))
        break;
