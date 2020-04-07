"Encryption algorithm to send a message"
import Point

class Encryption(object):

    "Curve: elliptic curve choosen, p: field where the curve is defined, h: number to trasform message, B: generator point"
    def __init__(self, c, p, h, B):
        self.curve=c
        self.p=p
        self.h=h
        self.B=B

    def encrypt(self, r, kprv, dkp):
        V = Point()

