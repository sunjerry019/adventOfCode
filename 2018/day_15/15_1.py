#!/usr/bin/env python3

import numpy as np
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from classes import myPath

class Problem():
    def __init__ (self):
        # note that 205128 is TOO LOW
        self.input = open("testcases/1.in", "r")
        self.inputContents = self.input.readlines()
        self.max_x = len(self.inputContents[0].strip())
        self.max_y = len(self.inputContents)

        self.karteMapping = {
            ".": 0,
            "#": 1,
            "G": 2,
            "E": 3
        }
        self.karteMappingR = {
            0: " ",
            1: "#",
            2: "G",
            3: "E"
        }

        # To be updated whenever a unit moves. A list of all shortest
        # distance and next coord to move
        # <k, v> = (tuple), {(tuple) : pathObject}
        # self.distances        = {}
        self.allUnits         = [] # Sorted in reading order of initial state (includes both elves and goblins)
        self.allUnitsCurrent  = {} # (origCoord) : currCoord
        self.allUnitsCurrentR = {} # (currCoord) : origCoord
        self.elves            = {} # (currCoord) : Health
        self.goblins          = {} # (currCoord) : Health

        self.map = np.zeros((self.max_x, self.max_y), dtype=int)


        for y in range(self.max_y):
            for x in range(self.max_x):
                obj = self.inputContents[y][x]
                self.map[x, y] = self.karteMapping[obj]
                if obj == "G":
                    self.goblins[(x,y)] = 200
                    self.allUnits.append((x,y))
                    self.allUnitsCurrent[(x,y)] = (x,y)
                    self.allUnitsCurrentR[(x,y)] = (x,y)
                if obj == "E":
                    self.elves[(x,y)] = 200
                    self.allUnits.append((x,y))
                    self.allUnitsCurrent[(x,y)] = (x,y)
                    self.allUnitsCurrentR[(x,y)] = (x,y)

        # path = self.findPath((1,1),(7,7))
        # print(path)

        self.rounds = 0
        self.turns = 0
        self.ended = False
        while not self.ended:
            self.rounds += 1
            self.runRound()

        self.unitsLeft = {**self.elves, **self.goblins}
        self.hitpoints = sum(self.unitsLeft.values())
        # print("\033[2KGame ended with {} full rounds, with final hitpoints of {} = {} ".format(self.rounds, self.hitpoints, self.rounds*self.hitpoints))

        # OUTPUT HERE
        print("{}\t{}\t{}".format(self.rounds, self.hitpoints, self.rounds*self.hitpoints))

    def accessible(self, unit):
        freespace = 0
        freespace += (self.map[unit[0] + 1, unit[1]    ] == 0)
        freespace += (self.map[unit[0]    , unit[1] + 1] == 0)
        freespace += (self.map[unit[0] - 1, unit[1]    ] == 0)
        freespace += (self.map[unit[0]    , unit[1] - 1] == 0)
        return (freespace > 0)

    def whichAccessible(self, unit):
        accessible = []
        if (self.map[unit[0]    , unit[1] - 1] == 0) : accessible.append((unit[0]    , unit[1] - 1))
        if (self.map[unit[0] - 1, unit[1]    ] == 0) : accessible.append((unit[0] - 1, unit[1]    ))
        if (self.map[unit[0] + 1, unit[1]    ] == 0) : accessible.append((unit[0] + 1, unit[1]    ))
        if (self.map[unit[0]    , unit[1] + 1] == 0) : accessible.append((unit[0]    , unit[1] + 1))
        return accessible # returns in reading order

    def enemiesNextToMe(self, unit):
        if unit in self.elves:
            enemy = 2
            referenceArray = self.goblins
        else:
            enemy = 3
            referenceArray = self.elves

        enemies = []    # Coord
        health = []     # Health
        if self.map[unit[0]    , unit[1] - 1] == enemy:
            enemies.append((unit[0]    , unit[1] - 1))
            health.append(referenceArray[(unit[0]    , unit[1] - 1)])
        if self.map[unit[0] - 1, unit[1]    ] == enemy:
            enemies.append((unit[0] - 1, unit[1]    ))
            health.append(referenceArray[(unit[0] - 1, unit[1]    )])
        if self.map[unit[0] + 1, unit[1]    ] == enemy:
            enemies.append((unit[0] + 1, unit[1]    ))
            health.append(referenceArray[(unit[0] + 1, unit[1]    )])
        if self.map[unit[0]    , unit[1] + 1] == enemy:
            enemies.append((unit[0]    , unit[1] + 1))
            health.append(referenceArray[(unit[0]    , unit[1] + 1)])

        return enemies, health

    def identifyEnemyUnits(self, unit):
        availableUnits = {}

        if unit in self.elves:
            searchArray = self.goblins
        else: # Goblin
            searchArray = self.elves

        for enemy in searchArray:
            if self.accessible(enemy):
                p = self.findPath(unit, enemy)
                if p.distance > 0:
                    if p.distance not in availableUnits:
                        availableUnits[p.distance] = {}
                    availableUnits[p.distance][enemy] = p

        return availableUnits

    def checkIfRoundHasEnded (self, unit):
        lastidx = len(self.allUnits) - 1
        idx = -1
        for i in range(lastidx, -1, -1):
            if self.allUnits[i] == unit:
                idx = i
                break
        if idx == lastidx:
            return True
        elif idx == lastidx - 1:
            if self.allUnits[lastidx] not in self.allUnitsCurrent:
                return True

        return False

    def runRound(self):
        for unit in self.allUnits:
            if unit in self.allUnitsCurrent:
                if not self.runTurn(unit):
                    # self.printMap()
                    if not self.checkIfRoundHasEnded(unit):
                        self.rounds -= 1
                    break;
                # self.printMap()
                # self.printProgress()

        self.turns = 0
        self.updateRound()

    def runTurn(self, unit):
        self.turns += 1
        # print(unit)
        currCoord = self.allUnitsCurrent[unit]

        # Check if not adjacent to enemy
        adjEnemies, adjHealth = self.enemiesNextToMe(currCoord)
        if not adjEnemies:
            # identify all the enemies that are reachable by the current unit
            # and for which there is some uninterrupted path
            enemies = self.identifyEnemyUnits(currCoord)

            if enemies:
                # get smallest distance
                closestEnemies = enemies[min(enemies)]
                # if got tie, break by current position
                if len(closestEnemies) > 1:
                    closestEnemy, pathToEnemy = self.minReadingOrder(closestEnemies)
                else:
                    closestEnemy, pathToEnemy = next(iter(closestEnemies.items()))

                pathToEnemy = self.checkWhichPath(currCoord, closestEnemy, pathToEnemy)

                # move along path
                newCoord = pathToEnemy.path[1]
                self.map[newCoord] = self.map[currCoord]
                self.map[currCoord] = 0
                # update selfArrays
                self.allUnitsCurrent[unit] = newCoord
                self.allUnitsCurrentR[newCoord] = unit

                if self.map[newCoord] == 3:
                    # Elf
                    self.elves[newCoord] = self.elves[currCoord]
                    del self.elves[currCoord]
                else:
                    # Goblin
                    self.goblins[newCoord] = self.goblins[currCoord]
                    del self.goblins[currCoord]

                # recalculate enemies next to me
                currCoord = newCoord
                adjEnemies, adjHealth = self.enemiesNextToMe(currCoord)
            else:
                # print(currCoord, "No enemies reachable")
                pass

        if adjEnemies:
            # if available -> attack
            lowestHealth = min(adjHealth)
            enemyToAttack = adjEnemies[adjHealth.index(lowestHealth)]

            isGoblin = (self.map[enemyToAttack] == 2)
            if isGoblin: # Goblin
                self.goblins[enemyToAttack] -= 3
            else: # Elf
                self.elves[enemyToAttack] -= 3

            # check if ded
            ded = False
            if isGoblin:
                if self.goblins[enemyToAttack] <= 0:
                    ded = True
                    del self.goblins[enemyToAttack]
            else:
                if self.elves[enemyToAttack] <= 0:
                    ded = True
                    del self.elves[enemyToAttack]

            if ded:
                del self.allUnitsCurrent[self.allUnitsCurrentR[enemyToAttack]]
                del self.allUnitsCurrentR[enemyToAttack]
                self.map[enemyToAttack] = 0

                # check if game has ended
                bc = np.bincount(self.map.flatten())
                if len(bc) < 4 or bc[2] == 0:
                    self.ended = True
                    return False

        return True

    def updateRound(self):
        self.allUnits        = []
        self.allUnitsCurrent = {}
        self.allUnitsCurrentR = {}

        for y in range(self.max_y):
            for x in range(self.max_x):
                obj = self.map[x, y]
                if obj == 2 or obj == 3:
                    self.allUnits.append((x,y))
                    self.allUnitsCurrent[(x,y)] = (x,y)
                    self.allUnitsCurrentR[(x,y)] = (x,y)

    def minReadingOrder(self, units):
        comparisonMap = {}
        for unit in units:
            comparisonMap[np.ravel_multi_index(unit, self.map.shape)] = unit
        minimum = comparisonMap[min(comparisonMap)]
        return minimum, units[minimum]

    def checkWhichPath (self, startCoord, enemyCoord, originalPath):
        availableSlots = self.whichAccessible(enemyCoord)
        availablePaths = []

        if len(availableSlots) == 1:
            return originalPath
        else:
            shortest = originalPath.distance
            for slot in availableSlots:
                p = self.findPath(startCoord, slot)
                if p.distance > 0:
                    if p.distance < shortest:
                        shortest = p.distance
                        availablePaths = [p]
                    elif p.distance == shortest:
                        availablePaths.append(p)

        if len(availablePaths) == 0:
            print("Uncaught Error, unable to find available path")
            quit()

        return availablePaths[0]

    def findPath(self, startCoord, endCoord):
        matrix = (self.map == 0).T.astype(int)
        # note here that the matrix is transposed
        matrix[startCoord[1], startCoord[0]] = 1
        matrix[endCoord[1], endCoord[0]] = 1
        # print(matrix)
        grid = Grid(matrix=matrix.tolist())

        start = grid.node(startCoord[0], startCoord[1])
        end = grid.node(endCoord[0], endCoord[1])

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

        path, runs = finder.find_path(start, end, grid)
        # print('operations:', runs, 'path length:', len(path))
        # print(grid.grid_str(path=path, start=start, end=end))

        p = myPath(startCoord, endCoord, len(path), path)
        return p

    def printProgress(self):
        print("Round = {}, Turn = {:>3}/{:>3}".format(self.rounds, self.turns, len(self.allUnitsCurrent)), end="\r")

    def printMap(self):
        print("-------------------------------------------")
        print("Round = {}, Turn = {:>3}/{:>3}".format(self.rounds, self.turns, len(self.allUnitsCurrent)))
        for y in range(self.max_y):
            for x in range(self.max_x):
                print(self.karteMappingR[self.map[x, y]], end="")
            print("")
        print("Globins:", self.goblins)
        print("Elves:  ", self.elves)
        print("-------------------------------------------")

Problem()
