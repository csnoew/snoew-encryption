from random import seed
from random import random
import time
import sys
import os
import secrets
i = 0
low = 1
high = 100000000000
output = ""

# watermark lol
print(" > snoew encryptor v1.0")

# input
key = input("Encryption key (type 0 for no key): ")
try:
    float(key)
except ValueError:
    print("This is not a valid key")
    time.sleep(1)
    os.startfile(__file__)
    sys.exit()

unencrypted: str = input("Message to encrypt: ")

# generate key
if key == "0":
    key = secrets.randbelow(high - low) + low

# encryption
while i < len(unencrypted):
    seed(unencrypted[i])
    ran = random()
    let = int(key) * ran
    output = output + str(let) + " "
    i = i + 1

print("")
print("-------------------")
print("Encryption complete")
print("Decryption key:")
print(key)
print("")
print("Encrypted message:")
print(output)
print("-------------------")
input("Press enter to exit...")
