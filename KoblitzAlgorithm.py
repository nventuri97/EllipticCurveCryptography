"Implementation of Koblitz's algorithm to trasform a message in a point of a elliptic curve"

import math
from Point import Point
from Exception.NonValidHException import NonValidHException

class KoblitzAlgorithm(object):

    def __init__(self, a, b, p):
        self.p=p
        self.a=a
        self.b=b

    def trasform_message(self, m, h):
        if (m+1)*h>=self.p:
            raise NonValidHException
        else:
            Pm=Point(-1,-1)
            for i in range(h):
                x=m*h+i
                y=math.sqrt((x**3+self.a*x+self.b)%self.p)%self.p
                if y.is_integer():
                    Pm.setX(x)
                    Pm.setY(y)
                    break
            return Pm