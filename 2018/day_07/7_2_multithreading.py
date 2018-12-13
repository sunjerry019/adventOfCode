#!/bin/python3

import numpy as np
import threading

input = open("7.in","r")
inputContents = input.readlines()
dependencies = {}
stepsCompleted = {}
steps = []
workers = []
workingOn = [""]*5
workStarted = [False]*5
zeit = 0

lock = threading.Lock()

stopAll = False
finishWorking = [threading.Event()] * 5
weiter = threading.Event()
ended = []

def dependenciesFulfilled(key):
    df = 0
    for dependency in dependencies[key]:
        if dependency in stepsCompleted:
            df += 1
    if df == len(dependencies[key].keys()):
        return True
    return False

class work(threading.Thread):
    def run(self):
        id = int(self.getName()) - 1
        #print("Worker {} started".format(id))
        while True:
            if zeit > 0:
                #print("Worker {}: waiting for weiter".format(id))
                weiter.wait()
                #print("Worker {}: weiter detected".format(id))
                finishWorking[id].clear()

                if workStarted[id]:
                    if zeit == workStarted[id] + (ord(workingOn[id]) - 4):
                        # print("\n", zeit, workStarted[id] + (ord(workingOn[id]) - 4))
                        lock.acquire()
                        stepsCompleted[workingOn[id]] = 1
                        # print(stepsCompleted)
                        steps.append(workingOn[id])
                        workingOn[id] = ""
                        workStarted[id] = False
                        lock.release()
                else:
                    stepsAvailable = []
                    for step in dependencies:
                        if (len(dependencies[step].keys()) == 0 or dependenciesFulfilled(step)) and step not in stepsCompleted and step not in workingOn:
                            stepsAvailable.append(step)
                    try:
                        stepToDo = min(stepsAvailable)
                        workingOn[id] = stepToDo
                        workStarted[id] = zeit
                    except:
                        if len(stepsCompleted.keys()) == len(dependencies.keys()):
                            print("Worker {}: done".format(id))
                            ended.append(id)
                            finishWorking[id].set()
                            return;
                # print("Doing Step {} from {}".format(stepToDo, stepsAvailable))

                if len(stepsCompleted.keys()) == len(dependencies.keys()):
                    print("Worker {}: done".format(id))
                    ended.append(id)
                    finishWorking[id].set()
                    return;

                finishWorking[id].set()
        # print("{}: working on step".format(self.getName()))

class runTimer(threading.Thread):
    def run(self):
        global zeit
        print("Timer Started")
        while True:
            # print(ended)
            if len(ended) == 5:
                print("Timer ended")
                return
            elif len(workers) == 5:
                print("t = {}, current steps = {}".format(zeit ,"".join(steps)), end="\r")
                zeit += 1
                weiter.set()
                for i in range(5):
                    finishWorking[i].wait()
                weiter.clear()



if __name__ == '__main__':
    for instruction in inputContents:
        a = instruction.split(" must be finished before step ")
        b = [a[0][-1], a[1][0]]
        if b[0] not in dependencies:
            dependencies[b[0]] = dict()
        if b[1] not in dependencies:
            dependencies[b[1]] = dict()
        dependencies[b[1]][b[0]] = 1

    timer = runTimer(name = "timer")
    timer.start()
    for x in range(5):
        worker = work(name = x + 1)         # ...Instantiate a thread and pass a unique ID to it
        worker.start()
        workers.append(worker)

    for w in workers:
        w.join()
    timer.join()

    print("t = {}, final steps = {}".format(zeit, "".join(steps)))
