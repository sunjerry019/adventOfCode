#!/bin/python3

import numpy as np
import copy

input = open("5.in","r")
polymer = list(input.readlines()[0].strip())
# polymer = list("dabAcCaCBAcCcaDA")

def react(poly):
    while True:
        reactions = 0
        i = 0
        while i < len(poly) - 1:
            # print("({:5d}/{:5d}) Pass {}".format(i, len(polymer), passes), end="\r")
            # print("".join(polymer))
            if poly[i].upper() == poly[i+1].upper() and poly[i] != poly[i+1]:
                #print("Deleting {}{}".format(polymer[i],polymer[i+1]))
                reactions = reactions + 1
                del poly[i]
                del poly[i] # index i+1 element becomes index i
            else:
                i = i + 1
        if reactions == 0:
            # print("{:<20}\n\nRemaining Polymer Length = {}".format("".join(po), len(p)))
            break
    return poly

def main():
    shortest = len(polymer)
    alphabets = [chr(ch) for ch in range(65, 91)]
    temp = []
    # newPoly = []
    q = 0
    for alphabet in alphabets:
        # temp.append([])
        # newPoly.append([])

        # q = q + 1
        # print("({:2d}/26) {}: ...".format(q, alphabet), end='\r')
        # temp[q-1] = [x for x in polymer if x.upper() != alphabet]
        # newPoly = react(temp[q-1])
        # if len(newPoly) < shortest:
        #     shortest = len(newPoly)
        # print("({:2d}/26) {}: Length = {}".format(q, alphabet, len(newPoly)))
        # print("".join(newPoly))

        q = q + 1
        print("({:2d}/26) {}: ...".format(q, alphabet), end='\r')
        newPoly = react(copy.deepcopy([x for x in polymer if x.upper() != alphabet]))
        if len(newPoly) < shortest:
            shortest = len(newPoly)
        print("({:2d}/26) {}: Length = {}".format(q, alphabet, len(newPoly)))
        # print("".join(newPoly))

    print("\nShortest Length = {}".format(shortest))

main()
