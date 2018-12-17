#!/usr/bin/env python3

import numpy as np

input = open("5.in","r")
polymer = list(input.readlines()[0].strip())
passes = 0

def react():
    global polymer, passes
    reactions = 0
    passes = passes + 1
    i = 0
    while i < len(polymer) - 1:
        print("({:5d}/{:5d}) Pass {}".format(i, len(polymer), passes), end="\r")
        #print("".join(polymer))
        if polymer[i].upper() == polymer[i+1].upper() and polymer[i] != polymer[i+1]:
            #print("Deleting {}{}".format(polymer[i],polymer[i+1]))
            reactions = reactions + 1
            del polymer[i]
            del polymer[i] # index i+1 element becomes index i
        else:
            i = i + 1
    return reactions

def main():
    while True:
        if react() == 0:
            print("{:<20}\n\n{} passes\nRemaining Polymer Length = {}".format("".join(polymer), passes, len(polymer)))
            break

main()
