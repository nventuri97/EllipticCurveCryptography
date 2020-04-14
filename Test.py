"""Test file"""
import math
import sys
from Point import Point
from KoblitzAlgorithm import KoblitzAlgorithm
from ECC import ECC

class Test(object):

    def main():
        print("Welcome in test class")
        a=14
        b=12
        p=129

        B=Point(1,2)
        encryptor=ECC(14,12,23, B)

        kprvM=11
        
        kprvD=7
        print("before")
        kpubD=encryptor.kpub_generator(kprvD)
        print("Public destination key is ", kpubD.getCoordinate())

        m=8
        h=11
        transformer=KoblitzAlgorithm(a,b,p)
        Pm=transformer.trasform_message(m,h)
        print("Pm is ",Pm.getCoordinate())
        if(Pm.X==-1):
            print("it's impossible to generate a point for this value of h")
        else:
            print("Now encrypt the message")
            pair=encryptor.encrypt(9, kpubD, Pm)
            print("Pair is ", pair)

            print("Now you have to decrypt message")
            PmD=encryptor.decrypt(pair, kprvD)
            print(PmD.getCoordinate())
            x=Pm.X
            mr=math.floor(x/h)
            print("Message received is ", mr)

    if __name__=="__main__":
        main()
