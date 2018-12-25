#!/usr/bin/env python3
import hashlib

eingabe = "iwrupvqb"
# eingabe = "abcdef"

i = 1
while True:
    print(i, end="\r")
    currKey = eingabe + str(i)
    hash = hashlib.md5(str.encode(currKey)).hexdigest()
    if hash[:5] == "00000":
        break
    i += 1

print(i)
