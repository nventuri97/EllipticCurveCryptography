import math
from Point import Point

"Encryption algorithm to send a message"
class Encryption(object):

    "Curve: elliptic curve choosen, p: field where the curve is defined, h: number to trasform message, B: generator point"
    def __init__(self, a, b, p, B):
        self.a=a
        self.b=b
        self.p=p
        self.B=B

    """Method used to calculate the gradient of passing line for A and B"""
    def __calc_lmb(self, A, B):
        if (A==B):
            return (3*A.getX**2+self.a)/(2*A.getY)
        else:
            return (B.getY-A.getY)/(B.getX-A.getX)

    """Method used to calculate the sum of two points"""
    def __sum_points(self, A, B):
        C= Point()

        xa= A.getX()
        ya= A.getY()
        xb= B.getX()

        lmb=self.__calc_lmb(A,B)

        xc=(lmb**2-xa-xb)%self.p
        yc=(-ya+lmb*(xa-xc))%self.p
        C.setX(xc)
        C.setY(yc)
        return C
        
    """Method which execute the redoubling method to calculate the product of an integer k per a point A"""
    def __redoubling_method(self, A, k):
        t=math.log2(k)
        kbin=k.bin()
        count=0
        R=[A]
        D=A
        for i in range(t):
            D=self.__sum_points(D,D)
            R.append(D)

        Q=Point()
        for i in kbin:
            if i==1:
                Q=self.__sum_points(Q, R.pop(count))
            count++
        return Q

    def encrypt(self, r, kprv, dkp, Pm):
        V=Point()
        W=Point()

        