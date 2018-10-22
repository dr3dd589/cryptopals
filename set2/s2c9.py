
from Crypto.Cipher import AES


def pad(message,n):
    if len(message) % n != 0:
        message = message + '%s'%(chr(n-len(message)%n))*(n - len(message)%n )
    return message


expected = "YELLOW SUBMARINE\x04\x04\x04\x04".encode('ascii')
padded = pad("YELLOW SUBMARINE".encode('ascii'), 20)
if expected == padded:
    print('True')