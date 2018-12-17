#!/usr/bin/env python3

import math

class Problem():
    def __init__ (self):
        self.rawinput = "074501"
        # self.rawinput = "51589"
        # self.rawinput = "59414"
        self.input = [int(x) for x in self.rawinput]
        # self.afterRecipe = 19
        self.recipeScores = [3, 7]
        self.elfRecipe = [0, 1]
        self.lastInsertion = list()
        self.found = False

        while not self.found:
            print(len(self.recipeScores), end="\r")
            score = self.recipeScores[self.elfRecipe[0]] + self.recipeScores[self.elfRecipe[1]]
            # print(self.recipeScores[self.elfRecipe[0]], self.recipeScores[self.elfRecipe[1]])
            # try:
            #     newRecipes = [(score//(10**i))%10 for i in range(math.ceil(math.log(score, 10)+0.001)-1, -1, -1)]
            # except:
            #     newRecipes = [0]
            if score > 9:
                newRecipes = [math.floor(score/10), score%10]
            else:
                newRecipes = [score]

            for digit in newRecipes:
                self.recipeScores.append(digit)
                if len(self.recipeScores) <= len(self.input):
                    self.lastInsertion = self.recipeScores
                else:
                    self.lastInsertion = self.recipeScores[-len(self.input):]
                if self.lastInsertion == self.input:
                    self.found = True
                    print(len(self.recipeScores) - len(self.input))
                    break;

            # Move Elves
            l = len(self.recipeScores)
            for i in range(2):
                self.elfRecipe[i] += 1 + self.recipeScores[self.elfRecipe[i]]
                self.elfRecipe[i] %= l

Problem()
