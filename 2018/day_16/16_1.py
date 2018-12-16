#!/bin/python3

import numpy as np
import copy

class Problem():
    def __init__ (self):
        self.input = open("16.in", "r")
        self.inputContents = self.input.readlines()
        self.opcodes = ["addr", "addi", "mulr", "muli", "banr", "bani", "borr", "bori", "setr", "seti", "gtir", "gtri", "gtrr", "eqir", "eqri", "eqrr"]
        self.opcodeMapping = np.zeros((16,)).tolist()

        # Get the input for the first part of the question
        self.it = 0
        self.threeOrMore = 0
        self.totalSamples = 0
        while len(self.inputContents[self.it].strip()) > 0:
            self.totalSamples += 1
            before    = np.array([int(x) for x in self.inputContents[self.it].strip().split("[")[1][:-1].split(", ")])
            self.it += 1
            operation = [int(x) for x in self.inputContents[self.it].strip().split(" ")]
            self.it += 1
            after     = np.array([int(x) for x in self.inputContents[self.it].strip().split("[")[1][:-1].split(", ")])
            self.it += 2

            possibilities = self.possibleOpCodes(before, operation, after)
            l = len(possibilities)
            if l == 1:
                self.opcodeMapping[operation[0]] = { possibilities[0] }

            if l > 1:
                if l >= 3:
                    self.threeOrMore += 1

                if self.opcodeMapping[operation[0]]:
                    if len(self.opcodeMapping[operation[0]]) > 1:
                        self.opcodeMapping[operation[0]] = self.opcodeMapping[operation[0]].intersection({ possibilities })
                else:
                    self.opcodeMapping[operation[0]] = { possibilities[0] }

        print("Part 1 = {}/{}".format(self.threeOrMore, self.totalSamples))

        self.opcodeMapping = [next(iter(s)) for s in self.opcodeMapping]

        # PART 2

        self.it += 2
        self.program = self.inputContents[self.it:]
        self.registers = np.zeros(4, dtype=np.uint64)
        for line in self.program:
            operation = [np.uint64(x) for x in line.strip().split(" ")]
            operation[0] = self.opcodeMapping[operation[0]]
            newReg = self.runOperation(copy.deepcopy(self.registers), operation)
            self.registers = newReg
            print(self.registers, operation)


        print("Part 2 = {}".format(self.registers))


    def possibleOpCodes(self, before, operation, after):
        possibilities = []
        for opcode in self.opcodes:
            o = copy.deepcopy(operation)
            o[0] = opcode
            reg = self.runOperation(copy.deepcopy(before), o)
            # print(before, o, reg, after)
            if np.array_equal(reg, after):
                possibilities.append(opcode)
        return possibilities


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
