#!/usr/bin/env python3

import numpy as np
import copy

class Problem():
    def __init__ (self):
        self.input = open("19.in", "r")
        self.inputContents = self.input.readlines()
        self.registers = np.zeros(6, dtype=int)

        self.ip = int(self.inputContents[0].strip().split(" ")[1])
        self.ipValue = 0
        self.instructions = [x.strip() for x in self.inputContents[1:]]
        self.iLength = len(self.instructions)

        self.iteration = 0
        while self.ipValue < self.iLength:
            self.iteration += 1
            self.registers[self.ip] = self.ipValue

            befehl = self.instructions[self.registers[self.ip]].split(" ")
            operation = [befehl[0]] + [int(x) for x in befehl[1:]]
            newReg = self.runOperation(copy.deepcopy(self.registers), operation)

            # print("\033[2Ki = {} ip={:>2} {}".format(self.iteration, self.registers[self.ip], self.registers),end='\r')
            print("\033[2Ki = {} ip={}".format(self.iteration, self.registers[self.ip]),end='\r')

            self.registers = newReg
            self.ipValue = self.registers[self.ip]
            self.ipValue += 1

        print("\033[2KHalted!")
        print("iterations = {}, ip = {} => {}".format(self.iteration, self.ipValue, self.registers))
        print("\a")



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
