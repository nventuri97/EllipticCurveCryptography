"""Base class Point"""
class Point(object):
    
    def __init__(self, x=0, y=0):
        self.X=x
        self.Y=y

    def getCoordinate(self):
        return (self.X, self.Y)

    def setX(self, value):
        self.X=value

    def getX(self):
        return self.X

    def setY(self, value):
        self.Y=value

    def getY(self):
        return self.Y