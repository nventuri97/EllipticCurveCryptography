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
                z=(pow(int(x),3,self.p)+int(x)*self.a+self.b)%self.p
                if self.__quadratic_residue(z)==1:
                    y=self.__tonelli(z, self.p)
                    Pm.setX(x)
                    Pm.setY(y)
                    break
            return Pm

    def __quadratic_residue(self, z):
        return pow(z, (self.p-1)//2, self.p)
    
    def __tonelli(self, n, p):
        q = p - 1
        s = 0
        while q % 2 == 0:
            q //= 2
            s += 1
        if s == 1:
            return pow(n, (p + 1) // 4, p)
        for z in range(2, p):
            if p - 1 == self.__quadratic_residue(z, p):
                break
        c = pow(z, q, p)
        r = pow(n, (q + 1) // 2, p)
        t = pow(n, q, p)
        m = s
        t2 = 0
        while (t - 1) % p != 0:
            t2 = (t * t) % p
            for i in range(1, m):
                if (t2 - 1) % p == 0:
                    break
                t2 = (t2 * t2) % p
            b = pow(c, 1 << (m - i - 1), p)
            r = (r * b) % p
            c = (b * b) % p
            t = (t * c) % p
            m = i
        return r