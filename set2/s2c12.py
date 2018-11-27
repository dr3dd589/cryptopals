from Crypto.Cipher import AES
from base64 import b64decode,b64encode
import random
import time

unknown_str = "Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBqdXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUgYnkK"

def pad(msg,l):
    if len(msg)%l != 0:
        a =  msg + chr(len(msg)%l)*(16-len(msg)%l)
        return a
    else:
        return msg

def random_key(l):
    return ''.join(chr(random.randint(0,256)) for i in range(l))

def encrypt(key,msg):
    cipher = AES.new(key,AES.MODE_ECB)
    return cipher.encrypt(msg)

def decrypt(key,msg):
    cp = AES.new(key,AES.MODE_ECB)
    return cp.decrypt(msg)

def main():
    key = random_key(16)
    flag = ""
    for i in range(1,140):
        known_str = "A"*(144-i)
        a = known_str + b64decode(unknown_str)
        msg = pad(a,16)
        encr_msg = encrypt(key,msg)

        for j in range(0,256):
            nice_output = flag + chr(j)
            time.sleep(.001)
            print(nice_output)
            em = "A"*(144-i) + nice_output
            em_encr = encrypt(key,em)
            if em_encr[128:] == encr_msg[128:144]:
                flag += chr(j)
                break

                

if __name__ == '__main__':
    main()
