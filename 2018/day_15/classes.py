#!/bin/python3

class myPath():
    def __init__(self, startCoord, endCoord, distance, path):
        # path is an array of coordinates to move to
        self.start = startCoord
        self.end = endCoord
        self.distance = distance
        self.path = path

        pass
    def __repr__(self):
        return "<" + " ".join([repr(self.start), repr(self.end), repr(self.distance)]) + ">"
