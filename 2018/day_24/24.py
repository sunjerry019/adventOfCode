#!/usr/bin/env python3

import math
import copy

class Group():
	def __init__(self, _id, _klasse, _units, _hp, _weakness, _immune, _damagePts, _damageType, _initiative):
		self.id = _id
		self.klasse = _klasse
		self.units = _units
		self.hp = _hp
		self.weakness = _weakness
		self.immune = _immune
		self.damagePts = _damagePts
		self.damageType = _damageType
		self.initiative = _initiative
		
	def __repr__(self):
		return "< Group {} (Type {}): \n  Units    = {}\n  HP       = {}\n  Weakness = {}\n  Immunity = {}\n  Damage   = {} x {}\n  Init     = {}\n>".format(self.id, self.klasse, self.units, self.hp, self.weakness, self.immune, self.damagePts, self.damageType, self.initiative)
	
	def effectivePower(self):
		return self.units * self.damagePts

class Problem():
	def __init__(self):
		self.input = open("24.in","r")
		self.inputContents = self.input.readlines()
		self.inputLength = len(self.inputContents)
		self.ordnung = ["Immune System", "Infection", "No Winner"]
		
		# 0 = immune system; 1 = infection
		self.armies = [{},{}]
		self.parseInput()
		self.originalArmies = copy.deepcopy(self.armies)
		
		# Part 1
		self.part1 = self.solve()
		print("{} wins, Part 1 = {}".format(self.ordnung[self.part1[0]], self.part1[1]))	
		
		# Part 2
		self.boost = 0 # equals to part 1 answer
		self.interval = 1000
		self.boosted = {}
		self.prevWinner = self.part1[0]
		self.prevAns = 0
		self.part2 = (0,0)
		while True: # (self.boost + self.interval) not in self.boosted
			self.boost += self.interval
			print("Boost = {}".format(self.boost))
			self.boosted[self.boost] = 1
			self.addBoost()
			w, a = self.solve()
			if w != self.prevWinner and abs(self.interval) != 1:
				# we change direction and reduce the step
				self.interval *= -0.5
				self.interval = math.ceil(self.interval)
			elif w != self.prevWinner:
				if w == 0:
					self.part2 = (0, a)
					break
				else:
					self.boost -= self.interval
					self.part2 = (0, self.prevAns)
					break
			self.prevWinner = w
			self.prevAns = a
		print("{} wins, Boost = {}, Part 2 = {}".format(self.ordnung[self.part2[0]], self.boost, self.part2[1]))	
	
	def addBoost(self):
		self.armies = copy.deepcopy(self.originalArmies)
		for uid in self.armies[0]:
			self.armies[0][uid].damagePts += self.boost
	
	def solve(self):
		self.rounds = 0
		self.prevTickAns = False
		while len(self.armies[0]) and len(self.armies[1]):
			self.rounds += 1
			print("Tick {}".format(self.rounds), end='\r')
			self.tick()
			s_w, s_a = self.calcAns()
			if self.prevTickAns and self.prevTickAns[1] == s_a:
				# no change
				return s_w, s_a
			self.prevTickAns = (s_w, s_a)

		return self.calcAns()
	
	def calcAns(self):
		_ul = 0
		_w = -1
		for i in range(2):
			for uid in self.armies[i]:
				_ul+= self.armies[i][uid].units
				if self.armies[i][uid].units > 0 and _w < 0:
					_w = i
				elif self.armies[i][uid].units > 0 and _w != i:
					_w = 2
		return _w, _ul
	
	def tick(self):
		# Target Selection
		self.selectTargets()
		# Attacking Phase
		self.attackTargets()
		
	def attackTargets(self):
		gesortiert2 = self.sortArmies("init")
		for _unitID in gesortiert2:
			if self.isAlive(_unitID) and _unitID in self.targetsR and self.isAlive(self.targetsR[_unitID]): # Can attack and enemy is alive
				klasse, u = self.getUnit(_unitID)
				enemy = klasse ^ 1
				_dmg = u.damagePts * u.units
				if u.damageType in self.armies[enemy][self.targetsR[_unitID]].immune:
					_dmg *= 0
				if u.damageType in self.armies[enemy][self.targetsR[_unitID]].weakness:
					_dmg *= 2
				
				_deltaU = _dmg // self.armies[enemy][self.targetsR[_unitID]].hp
				self.armies[enemy][self.targetsR[_unitID]].units -= _deltaU
				
				# check if ded
				if self.armies[enemy][self.targetsR[_unitID]].units <= 0:
					del self.armies[enemy][self.targetsR[_unitID]]
					
					# Check if anybody else alive
					if not len(self.armies[enemy]):
						return False
		return True
					
	def selectTargets(self):
		gesortiert = self.sortArmies("ep-init")
		self.targets = {}   # <k,v> = Target, Attacker
		self.targetsR = {}  # <k,v> = Attacker, Target
		for _unitID in gesortiert:
			klasse, u = self.getUnit(_unitID)
			enemy = klasse ^ 1
			
			chosenTargets = []
			maxDamage = 0
			availableTargets = [q for q in self.armies[enemy].keys() if q not in self.targets]
			basicDamage = u.units * u.damagePts
			for t in availableTargets:
				_d = basicDamage
				if u.damageType in self.armies[enemy][t].immune:
					_d *= 0
				if u.damageType in self.armies[enemy][t].weakness:
					_d *= 2
				if _d > 0:
					if _d > maxDamage:
						maxDamage = _d
						chosenTargets = [t]
					elif _d == maxDamage:
						chosenTargets.append(t)

			if len(chosenTargets) == 0:
				continue
			
			if len(chosenTargets) > 1:
				# tie break by effective power
				maxEPArr = []
				maxEP = 0
				for t in chosenTargets:
					_ep = self.armies[enemy][t].effectivePower()
					if _ep > maxEP:
						maxEP = _ep
						maxEPArr = [t]
					elif _ep == maxEP:
						maxEPArr.append(t)
				chosenTargets = maxEPArr
				
			if len(chosenTargets) > 1:
				# tie break by initiative
				maxInitArr = []
				maxInit = 0
				for t in chosenTargets:
					_init = self.armies[enemy][t].initiative
					if _init > maxInit:
						maxInit = _init
						maxInitArr = [t]
					elif _init == maxInit:
						maxInitArr.append(t)
				chosenTargets = maxInitArr
				
			if len(chosenTargets) == 1:
				self.targets[chosenTargets[0]] = _unitID
				self.targetsR[_unitID] = chosenTargets[0]
			else:
				print("Something went wrong, _UnitID = {}, chosenTargets = {}".format(_unitID, chosenTargets))
				quit()
		
		
				
	def isAlive(self, unitID):
		return unitID in self.armies[0] or unitID in self.armies[1]
			
	def getUnit(self, unitID):
		a = int(unitID.split("_")[0])
		return a, self.armies[a][unitID]
		
	def sortArmies(self, _type="ep-init"):
		# combine the 2 armies into a sane dictionary
		ret = {}
		if _type == "ep-init":
			effPowers = {}
			for i in range(2):
				for _unit in self.armies[i]:
					_EP = self.armies[i][_unit].effectivePower()
					if _EP in effPowers:
						effPowers[_EP].append(_unit)
					else:
						effPowers[_EP] = [_unit]
			for p in effPowers:
				if len(effPowers[p]) == 1:
					ret[effPowers[p][0]] = p
				else:
					_tmpCount = 0
					for u in effPowers[p]:
						ret[effPowers[p][_tmpCount]] = p + self.armies[int(u.split("_")[0])][u].initiative/100
						_tmpCount += 1
		elif _type == "init":
			inits = {}
			for i in range(2):
				for _unit in self.armies[i]:
					ret[_unit] = self.armies[i][_unit].initiative
		else:
			print("Undefined sort type {}".format(_type))
			quit()
		
		return sorted(ret, key=ret.get, reverse=True)
	
	def printStatus(self):
		for i in range(2):
			print(self.ordnung[i])
			for uid in self.armies[i]:
				print("Group {} contains {} units".format(uid, self.armies[i][uid].units))
	
	def parseInput(self):
		self.it = -1
		for i in range(2):
			self.it += 2
			n = 0
			while self.it < self.inputLength and self.inputContents[self.it].strip() != "":
				a = self.inputContents[self.it].strip().split(" units each with ")
				_units = int(a[0])
				b = a[1].split(" hit points ")
				_hp = int(b[0])
				_immune = {}
				_weakness = {}
				if b[1][0] == "(":
					c = b[1][1:].split(") ")
					c1 = c[0].split("; ")
					for prop in c1:
						c2 = prop.split(" to ")
						if c2[0] == "immune":
							c3 = c2[1].split(", ")
							for elem in c3:
								_immune[elem] = 1
						elif c2[0] == "weak":
							c3 = c2[1].split(", ")
							for elem in c3:
								_weakness[elem] = 1
					d = c[1]
				else:
					d = b[1]
				e = d[25:].split(" damage at initiative ")
				f = e[0].split(" ")
				_damagePts = int(f[0])
				_damageType = f[1]
				_initiative = int(e[1])
				
				_group = Group(n, i, _units, _hp, _weakness, _immune, _damagePts, _damageType, _initiative)
				self.armies[i][str(i) + "_" + str(n)] = _group
				n += 1
				self.it += 1
		
Problem()
