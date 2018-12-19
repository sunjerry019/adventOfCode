#!/usr/bin/env python3

import numpy as np

class Problem():
    def __init__ (self):
        self.input = open("19.in", "r")
        self.inputContents = self.input.readlines()
        self.registers = np.zeros(6, dtype=int)
        self.registers[0] = 1

        self.ip = int(self.inputContents[0].strip().split(" ")[1])
        self.ipValue = 0
        self.instructions = [x.strip() for x in self.inputContents[1:]]
        self.iLength = len(self.instructions)

        self.iteration = 0
        self.previousMax = float('-inf')
        self.maxCount = 0

        while self.ipValue < self.iLength:
            if self.maxCount > 100:
                break
            self.iteration += 1
            self.registers[self.ip] = self.ipValue

            befehl = self.instructions[self.registers[self.ip]].split(" ")
            operation = [befehl[0]] + [int(x) for x in befehl[1:]]
            newReg = self.runOperation(np.copy(self.registers), operation)

            print("\033[2Ki = {:>4} ip={:>2} {} {} {}".format(self.iteration, self.registers[self.ip], self.registers, operation, newReg),end='\r')
            # print("\033[2Ki = {} ip={}".format(self.iteration, self.registers[self.ip]),end='\r')

            self.registers = newReg
            self.ipValue = self.registers[self.ip]
            self.ipValue += 1

            currMax = np.max(self.registers)
            if currMax == self.previousMax:
                self.maxCount += 1
            elif currMax > self.previousMax:
                self.previousMax = currMax
                self.maxCount = 0

        self.n = np.max(self.registers)
        print("\033[2Kiterations = {}, ip = {} => {}".format(self.iteration, self.ipValue, self.registers))
        print("Calculating sum of factors for {}".format(self.n))
        print("Part 2 = {}".format(sum(self.findFactors(self.n))))


        # print("\a")

    def findFactors(self, n):
        results = set()
        for i in range(1, int(np.sqrt(n)) + 1):
            if n % i == 0:
                results.add(i)
                results.add(n//i)
        return results

    def runOperation(self, registers, operation):
        if operation[0] == "addr":
            registers[operation[3]] = registers[operation[1]] + registers[operation[2]]
        elif operation[0] == "addi":
            registers[operation[3]] = registers[operation[1]] + operation[2]

        elif operation[0] == "mulr":
            registers[operation[3]] = registers[operation[1]] * registers[operation[2]]
        elif operation[0] == "muli":
            registers[operation[3]] = registers[operation[1]] * operation[2]

        elif operation[0] == "banr":
            registers[operation[3]] = registers[operation[1]] & registers[operation[2]]
        elif operation[0] == "bani":
            registers[operation[3]] = registers[operation[1]] & operation[2]

        elif operation[0] == "borr":
            registers[operation[3]] = registers[operation[1]] | registers[operation[2]]
        elif operation[0] == "bori":
            registers[operation[3]] = registers[operation[1]] | operation[2]

        elif operation[0] == "setr":
            registers[operation[3]] = registers[operation[1]]
        elif operation[0] == "seti":
            registers[operation[3]] = operation[1]

        elif operation[0] == "gtir":
            registers[operation[3]] = (operation[1] > registers[operation[2]])
        elif operation[0] == "gtri":
            registers[operation[3]] = (registers[operation[1]] > operation[2])
        elif operation[0] == "gtrr":
            registers[operation[3]] = (registers[operation[1]] > registers[operation[2]])

        elif operation[0] == "eqir":
            registers[operation[3]] = (operation[1] == registers[operation[2]])
        elif operation[0] == "eqri":
            registers[operation[3]] = (registers[operation[1]] == operation[2])
        elif operation[0] == "eqrr":
            registers[operation[3]] = (registers[operation[1]] == registers[operation[2]])

        return registers


Problem()
