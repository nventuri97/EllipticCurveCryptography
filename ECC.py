import math
from Point import Point
from Exception.PointToInfiteException import PointToInfiteException
from Exception.NoCurvePointException import NoCurvePointException

"""Define the main method to exchange message on Elliptic Curve"""
class ECC(object):

    """a, b: value of elliptic curv Ep(a,b), p: curve order, B: curve point choosen"""
    def __init__(self, a, b, p, B):
        self.a=a
        self.b=b
        self.p=p
        self.B=B
        if(self.__check(self.B)):
            self.n=self.__calc_ord(self.B)
            print(self.n)
        else:
            raise NoCurvePointException

    """Method to check if a point B belongs to the curve"""
    def __check(self, B):
        x=B.X
        y=math.sqrt((x**3+self.a*x+self.b)%self.p)%self.p
        if B.Y==y:
            return True
        else:
            return False

    """Method to calculate the order of a point"""
    def __calc_ord(self, B):
        i=2
        while(True):
            try:
                self.__redoubling_method(B,i)
            except:
                break
            i+=1
        return i    

    """Method to generate the inverse -A of a point A"""
    def __gen_Inverse(self, A):
        W=Point(A.getX(), self.p-A.getY())
        return W

    """Method used to calculate the gradient of passing line for A and B"""
    def __calc_lmb(self, A, B):
        xa=A.X
        ya=A.Y
        if A==B:
            if ya==0:
                raise PointToInfiteException
            else:
                yaopp=pow(2*ya, self.p-2,self.p)
                lmb=((3*xa**2+self.a)*yaopp)%self.p
                return lmb
        else:
            xb=B.X
            yb=B.Y
            if (xb-xa)==0:
                raise PointToInfiteException
            else:
                diffOpp=pow(int(xb-xa), self.p-2, self.p)
                lmb=((yb-ya)*diffOpp)%self.p
                return lmb

    """Method used to calculate the sum of two points"""
    def __sum_points(self, A, B):
        gradient=self.__calc_lmb(A,B)
        
        xa=A.X
        ya=A.Y
        if A==B:
            xc=(gradient**2-2*xa)%self.p
            yc=(-ya+gradient*(xa-xc))%self.p
            C=Point(xc, yc)
            return C
        else:
            xb=B.X
            yb=B.Y
            xc=(gradient**2-xa-xb)%self.p
            yc=(-ya+gradient*(xa-xc))%self.p
            C=Point(xc,yc)
            return C
        
    """Method which execute the redoubling method to calculate the product of an integer k per a point A"""
    def __redoubling_method(self, A, k):
        kbin=bin(k)
        kbin=kbin[2:]
        R=[A]
        D=A
        Q=Point()
        count=0
        for i in kbin[2:]:
            D=self.__sum_points(D,D)
            R.append(D)
            if i=="1":
                Q=self.__sum_points(Q,R.pop(count))
            count+=1
        return Q

    """Method to encypt Pm and generate the pair <V,W> to send"""
    def encrypt(self, r, Pdest, Pm):
        V=self.__redoubling_method(self.B,r)
        Q=self.__redoubling_method(Pdest, r)
        W=self.__sum_points(Pm,Q)
        return (V,W)

    """Method to decrypt and get Pm from pair <V,W>"""
    def decrypt(self, pair, kprv):
        V=pair[0]
        W=pair[1]
        Vf=self.__redoubling_method(V,kprv)
        Vff=self.__gen_Inverse(Vf)
        Pm=self.__sum_points(W,Vff)
        return Pm


    """Method to generate a public key from a private key given"""
    def kpub_generator(self, kprv):
        return self.__redoubling_method(self.B, kprv)