#!/usr/bin/env python3

input = open("1.in","r")
inputContents = input.readlines()
#inputContents = "+7, +7, -2, -7, -4".split(", ")

freq = 0
foundFreqs = [0]
found = False

loops = 0

while not found:
    loops = loops + 1
    for line in inputContents:
        freq = freq + int(line)
        print("Loop {}\tCurrent Freq {} Hz          ".format(loops, freq), end='\r', flush=True)
        if freq in foundFreqs:
            found = True
            print("Loop {}\tCurrent Freq {} Hz < encountered again >\n".format(loops, freq), flush=True)
            break
        else:
            foundFreqs.append(freq)

print(freq)
