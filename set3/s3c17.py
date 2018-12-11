from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
from Crypto.Random import get_random_bytes
import random



key = get_random_bytes(16)
iv = get_random_bytes(16)

def xor(a,b):
	return ''.join([chr(ord(a[i])^ord(b[i%len(b)])) for  i in range(len(a))])

def encrypt_data(data):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    enc = cipher.encrypt(pad(data,16,style='pkcs7'))
    return enc

def decrypt_data(encryptedParams):
    cipher = AES.new(key, AES.MODE_CBC,iv)
    paddedParams = cipher.decrypt(encryptedParams)
    try:
        params = unpad(paddedParams,16,style='pkcs7')
        return "True"
    except:
        return "False"

def oracle_attack(enc_msg):
    msg_block = []
    for i in range((len(enc_msg)/16)):
        msg_block.append(enc_msg[16*i:16*i+16])
    
    prev = iv
    plantext = ""
    for j in range(len(msg_block)):
        ccc = ""
        p = ""
        block = msg_block[j]
        for k in range(1,17):
            for i in range(256):
                c = "\x00"*(16-k) + chr(i) + ccc + block
                pad_err = decrypt_data(c)
                if pad_err =='True':
                    aaa = i^k
                    p = chr(aaa)+p
                    ccc = xor(p,chr(k+1)*k)
                    break
        plantext += xor(p,prev)
        prev = block
    return unpad(plantext,16,style='pkcs7')




def main():
    randome_arr = []
    with open('random.txt') as f:
        for line in f:
            randome_arr.append(line.strip())
    rand_msg = randome_arr[random.randrange(len(randome_arr)-1)].decode('base64')
    enc  = encrypt_data(rand_msg)
    print(oracle_attack(enc))


if __name__ == '__main__':
    main()
