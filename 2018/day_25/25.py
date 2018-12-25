#!/usr/bin/env python3

import math
import copy

class Problem():
	def __init__(self):
		self.input = open("25.in","r")
		self.inputContents = self.input.readlines()

		self.constellations = {}
		self.constCount = 0

		for line in self.inputContents:
			s = tuple(int(x) for x in line.strip().split(","))
			found = 0
			idxFound = []
			for konst in self.constellations:
				for star in self.constellations[konst]:
					if self.distance(star, s) <= 3:
						if konst not in idxFound:
							idxFound.append(konst)
							found += 1
			if found == 0:
				self.constellations[self.constCount] = [s]
				self.constCount += 1
			elif found == 1:
				self.constellations[konst].append(s)
			elif found > 1:
				for idx in idxFound:
					if idx != idxFound[0]:
						# print("<{}> {}".format(idxFound[0], idx), end=", ")
						self.constellations[idxFound[0]] += self.constellations[idx]
						del self.constellations[idx]
			# print("")

		print("Part 1 = {}".format(len(self.constellations)))


	def distance(self, coord1, coord2):
		_d = 0
		for i in range(len(coord1)):
			_d += abs(coord1[i] - coord2[i])
		return _d

Problem()
