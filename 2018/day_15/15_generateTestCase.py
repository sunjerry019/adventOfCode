#!/bin/python3

from secrets import randbelow
import numpy as np

karteMappingR = {
    0: ".",
    1: "#",
    2: "G",
    3: "E"
}

N = 1
max_size = 32
units = 30

output = open("testcases/differentResults", "w+")

for i in range(N):
    print("Testing Case [{:>4}/{:>4}]".format(i + 1, N))
    testfile = open("testcases/1.in", "w+")
    size = randbelow(max_size - 4) + 5

    for y in range(size):
        line = []
        for x in range(size):
            if x == 0 or y == 0 or x == size - 1 or y == size - 1:
                line.append("#")
            else:
                while True:
                    ch = randbelow(3)
                    if ch < 2:
                        break
                    elif ch == 2 and units > 0:
                        ch = randbelow(2) + 2
                        units -= 1
                        break

                line.append(karteMappingR[ch])

        testfile.write("{}\n".format("".join(line)))
    testfile.close()



output.close()
