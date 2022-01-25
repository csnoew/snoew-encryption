from random import seed
from random import random
import time
import sys
import os

ran = ""

# watermark lol
print(" > snoew decryptor v1.0")

# input
key = input("Decryption key: ")
try:
    float(key)
except ValueError:
    print("Invalid key")
    time.sleep(1)
    os.startfile(__file__)
    sys.exit()

encrypted: str = input("Message to decrypt: ")
alphabet: str = "abcdefghijklmnopqrstuvwxyzæøå1234567890,.-<>_?!#¤%&/()=+*^~¨´`|}][{$£@½§\:;' "
i: int = -1
g: int = 0


def alphatest():
    i2 = -1
    while i2 < len(alphabet):
        if i >= len(encrypted):
            print("-------------------")
            input("Press enter to exit...")
            exit()
        else:
            testletter = encrypted.split()[i]
            i2 += 1
            seed(alphabet[i2])
            let = int(key) * random()
        if str(let) == str(testletter):
            print(alphabet[i2], end='')
            txt.write(str(alphabet[i2]))
            i2 = len(alphabet)


txt= open("decryptions.txt", "a")
txt.write("key = " + str(key) + '\n')
txt.write("message = ")
print("")
print("-------------------")
print("Decrypted message: ")
while g != len(encrypted.split()):
    i += 1
    g += 1
    alphatest()
print("")
print("-------------------")
txt.write("\n" "\n")
txt.close()
input("Press enter to exit...")
