from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes



key = get_random_bytes(16)
iv = get_random_bytes(16)

def encrypt_data(data):
    data = data.replace(';', '%3B').replace('=', '%3D')
    x1 = 'comment1=cooking%20MCs;userdata='
    x2 = ';comment2=%20like%20a%20pound%20of%20bacon'
    params = x1 + data.encode('ascii') + x2
    cipher = AES.new(key, AES.MODE_CBC,iv)
    enc = cipher.encrypt(pad(params,16,style='pkcs7'))
    return enc

def decrypt_data(encryptedParams):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    paddedParams = cipher.decrypt(encryptedParams)
    params = unpad(paddedParams,16,style='pkcs7')
    return params

x = list(encrypt_data('AAAAAAAAAAAAAAAA?admin?true?AAAA'))

x[32]  = chr(4^ord(x[32]))
x[38] = chr(2^ord(x[38]))
x[43] = chr(4^ord(x[43]))
dec = decrypt_data(''.join(x))

if ";admin=true;"  in dec:
    print('Success!!.........\n')
    print(dec)