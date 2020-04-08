"""Base class Point"""
class Point(object):

    def __init__(self):
        self.X=0
        self.Y=0
    
    def __init__(self, x, y):
        self.X=x
        self.Y=y

    def setX(self, value):
        self.X=value

    def getX(self):
        return self.X

    def setY(self, value):
        self.Y=value

    def getY(self):
        return self.Y

    def opposite(self, p):
        W=Point()
        W.setX(self.getX)
        W.setY(p-self.getY)
        return W