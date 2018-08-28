import binascii
string = msg = """Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal"""

key = "ICE"

def xor_with_key():
   
    chrs = [chr(ord(string[i])^ord(key[i%len(key)]))for i in range(len(string))]
   
    enc_text = ''.join(chrs)
    s = binascii.hexlify(enc_text)
    return s  

if __name__=='__main__':
    print(xor_with_key())
