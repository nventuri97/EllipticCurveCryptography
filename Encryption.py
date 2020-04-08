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
        xa=A.getX()
        ya=A.getY()
        if (A==B):
            return (3*xa**2+self.a)/(2*ya)
        else:
            xb=B.getX()
            yb=B.getY()
            return (yb-ya)/(xb-xa)

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
        t=int(math.floor(math.log(2,k)))
        kbin=bin(k)
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
            count+=1
        return Q

    """Method to encypt Pm and generate the pair <V,W> to send"""
    def encrypt(self, r, kprv, Pdest, Pm):
        V=self.__redoubling_method(self.B, r)
        U=self.__redoubling_method(Pdest, r)
        W=self.__sum_points(Pm, U)
        return (V,W)

    """Method to decrypt and get Pm from pair <V,W>"""
    def decrypt(self, pair, kprv):
        V=pair[0]
        W=pair[1]
        L=V.getOppisite(self.p)
        Pm=self.__sum_points(W, self.redoubling_method(L,kprv))
        return Pm

    def kpub_generator(self, kprv):
        return self.__redoubling_method(self.B, kprv)