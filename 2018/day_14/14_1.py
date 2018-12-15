#!/bin/python3

import math

class Problem():
    def __init__ (self):
        self.afterRecipe = 74501 + 10
        # self.afterRecipe = 19
        self.recipeScores = [3, 7]
        self.elfRecipe = [0, 1]

        while len(self.recipeScores) < self.afterRecipe:
            score = self.recipeScores[self.elfRecipe[0]] + self.recipeScores[self.elfRecipe[1]]
            # print(self.recipeScores[self.elfRecipe[0]], self.recipeScores[self.elfRecipe[1]])
            try:
                # https://stackoverflow.com/a/21270442
                # added 0.001 to handle powers of 10
                newRecipes = [(score//(10**i))%10 for i in range(math.ceil(math.log(score, 10)+0.001)-1, -1, -1)]
            except:
                newRecipes = [0]
            self.recipeScores += newRecipes

            # Move Elves
            l = len(self.recipeScores)
            for i in range(2):
                self.elfRecipe[i] += 1 + self.recipeScores[self.elfRecipe[i]]
                self.elfRecipe[i] %= l

        for i in range(self.afterRecipe - 10, self.afterRecipe):
            print(self.recipeScores[i], end="")
        print("")
Problem()
