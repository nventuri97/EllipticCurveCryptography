import math

"""Base class Point"""
class Point(object):

    def __init__(self):
        self.X=0
        self.Y=0

    def setX(self, value):
        self.X=value

    def getX(self):
        return self.X

    def setY(self, value):
        self.Y=value

    def getY(self):
        return self.Y