from avalanche import mainA
from pad import pad_message
from shorten import shorten
import numpy as np

def unlist(lst):
    return ' '.join(map(str, lst))

#main hashing function
def hash(message, public_key):
    hashed = 0
    counter = 0
    if len(str(message)) > len(str(public_key)):
        diff = len(str(message)) - len(str(public_key))
        message = shorten(message, diff)
    try: 
        for char in message: 
            if char == " ":
                continue
            char = int(char)
            char *= public_key[counter]
            hashed += char
            counter += 1
    except IndexError:
        pass

    return hashed

#further encryption for smaller messages needing to be more secure
def encrypt(message, security):
    np.random.seed(int(security))
    ans = []
    message = str(message)
    for i in message:
        num = np.random.randint(1, 1000000)
        encrypted_char = ord(i) * num
        ans.append(encrypted_char)
    ans = unlist(ans)
    return ans
            
def main(message, public_key, security):
    message = mainA(message, security)
    if len(str(message)) <= 1000 and security > 100:
        message = encrypt(message, security)
    message = pad_message(message)
    hashed1 = hash(str(message), public_key)
    hashed2 = hash(str(hashed1), public_key)
    return hashed2
