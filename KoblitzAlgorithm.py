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
                x=(m*h+i)%self.p
                z=(pow(int(x),3)+int(x)*self.a+self.b)%self.p
                print("Z is ", z)
                if self.__quadratic_residue(z):
                    y=int(math.sqrt(z))
                    print((y**2)%self.p==(pow(int(x),3)+int(x)*self.a+self.b)%self.p)
                    Pm.setX(x)
                    Pm.setY(y)
                    break
            return Pm
    
    def __quadratic_residue(self, z):
        v=int(((self.p-1)//2)%self.p)
        x=pow(int(z), int(v), self.p)
        print("P is ", self.p)
        print("X is ", x)
        if x==1:
            return True
        return False