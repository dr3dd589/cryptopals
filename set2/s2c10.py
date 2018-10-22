from  Crypto.Cipher import AES
from base64 import b64decode

def decrypt(key,msg):
    iv = '0'*16
    cipher = AES.new(key,AES.MODE_CBC,iv)
    return cipher.decrypt(msg)

if __name__ == '__main__':
    key = "YELLOW SUBMARINE"
    with open('10.txt','r') as f:
        ciphertext = b64decode(''.join([line.strip() for line in f.readlines()]))
    print(decrypt(key,ciphertext))
