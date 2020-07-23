"""Test file for secp192r1"""
from multiprocessing import Pool, cpu_count
import itertools
import numpy as np
import math
import sys
import random
import matplotlib.pyplot as plt
import base64
from Point import Point
from KoblitzAlgorithm import KoblitzAlgorithm
from ECC import ECC


def parallelize(arr, func, n_cores=cpu_count()):
    arr_split = np.array_split(arr, n_cores)
    pool = Pool(n_cores)
    arr = list(itertools.chain(pool.map(func, arr_split)))
    pool.close()
    pool.join()
    res = []
    for a in arr:
        res = res + a
    return res


print("-------------------Elliptic curve cryptography-------------------")
print("-----encryption and decryption of an image using secp192-r1------")
print("-------------developed in Python from Nicola Venturi-------------")
print("-----------------------------------------------------------------")
print("\n")

"""I'm reading an image and trasfom it into a string"""
with open("./python-1-226045.png", "rb") as image:
    b64string = base64.b64encode(image.read())

"""Decode the string into ascii and trasform this string in a ascii character array"""
message = b64string.decode('ascii')
# message='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'
msg = []
for c in message:
    msg.append(ord(c))

"""Curve on p-192r1"""

p = int(2**192-2**64-1)
a = int('FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEFFFFFFFFFFFFFFFC', 16)
b = int('64210519E59C80E70FA7E9AB72243049FEB8DEECC146B9B1', 16)
gx = int('188DA80EB03090F67CBF20EB43A18800F4FF0AFD82FF1012', 16)
gy = int('07192B95FFC8DA78631011ED6B24CDD573F977A11E794811', 16)
G = Point(gx, gy)
n = int('FFFFFFFFFFFFFFFFFFFFFFFF99DEF836146BC9B1B4D22831', 16)
h = int('01', 16)
seed = int('3045AE6FC8422F64ED579528D38120EAE12196D5', 16)

print("-------------------Curve parameters------------------------------")
print("-----------------------------------------------------------------")
print("Odd prime p is ", p, "\n")
print("Value of a is ", a, "\n")
print("Value of b is ", b, "\n")
print("Generator point G is ", G.getCoordinate(), "\n")
print("Point order is ", n, "\n")
print("Starting value of h is ", h, "\n")
print("Seed for random value is ", seed, "\n")

# Curve setting and keys generation
encryptor = ECC(a, b, p, G, n, h, seed)
random.seed(seed)

print("-------------------Keys generation-----------------------------")
print("---------------------------------------------------------------")
(kprvM, kpubM) = encryptor.keys_generator()
print("Mitt keys are: ")
print("Private key ", kprvM)
print("Public key ", kpubM.getCoordinate())
print("---------------------------------------------------------------")
(kprvD, kpubD) = encryptor.keys_generator()
print("Dest keys are: ")
print("Private key ", kprvD)
print("Public key ", kpubD.getCoordinate())
print("---------------------------------------------------------------")
print("\n")

transformer = KoblitzAlgorithm(a, b, p)
trovato = False
ErrPoint = Point(-1, -1)
# Trasform every characters of the message in curve point if it is possible
while not trovato:
    p_message = []
    for i in msg:
        Pm = transformer.trasform_message(i, h)
        plt.plot(Pm.X, Pm.Y, marker='.')
        # If Pm is (-1,-1), it's not a curve point and it can't be added to the array
        if Pm.equals(ErrPoint):
            break
        p_message.append(Pm)
    if p_message.__len__() != msg.__len__():
        print("It's impossible to generate a point for this value of h ", h)
        h += 1
    else:
        trovato = True
        print("Right value of h is ", h)

"""Plot settings and show"""
plt.title("Message points generated with Koblitz algorithm")
plt.show(block=False)

# Message encryption simulation
print("Now encrypt the message")
encrypted_message = []
print(len(p_message))
count = 0


def encrypt(points):
    res = []
    for point in points:
        r = random.randint(2, n-1)
        V, W = encryptor.encrypt(r, kpubD, point)
        res.append((V, W))
    return res


def decrypt(list_of_couple):
    res = []
    for couple in list_of_couple:
        c = encryptor.decrypt(couple, kprvD)
        res.append(c)
    return res


encrypted_message = parallelize(p_message, encrypt)
for V, W in encrypted_message:
    # for every point i'll use a different r to have different pair on same points
    plt.plot(V.X, V.Y, marker='.')
    plt.plot(W.X, W.Y, marker='.')
    count += 1

plt.title("Points pair generated by the encryption method")
plt.show(block=False)

# Message decryption simulation
print("Now you have to decrypt message")
decrypt_message = parallelize(encrypted_message, decrypt)

msgrcv = list(map(lambda point: math.floor(point.X//h), decrypt_message))
s = "".join([chr(c) for c in msgrcv])

print(s == message)
imagedata = base64.b64decode(s)
image = 'new_image.png'
with open(image, 'wb') as f:
    f.write(imagedata)
