from Crypto.Cipher import AES

key = "YELLOW SUBMARINE"

def decrypt(key, plain):
    cipher = AES.new(key, AES.MODE_ECB )
    return cipher.decrypt(plain)



with open("7.txt") as f:
    lines = f.readlines()
lines = ''.join(lines)

enc_msg = lines.decode('base64')
msg = decrypt(key,enc_msg).decode('utf-8')
print(msg)
