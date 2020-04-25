"""Base class Point"""
class Point(object):
    
    def __init__(self, x=0, y=0):
        self.X=int(x)
        self.Y=int(y)

    def getCoordinate(self):
        return (self.X, self.Y)

    def setX(self, value):
        self.X=int(value)

    def getX(self):
        return self.X

    def setY(self, value):
        self.Y=int(value)

    def getY(self):
        return self.Y