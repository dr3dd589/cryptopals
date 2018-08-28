
import binascii

def xor(p, q):
    if len(p) != len(q):
        print("Lenght are not equal.!")

    return bytearray(a ^ b for a, b in zip(p, q))


if __name__ == '__main__':

    a = "1c0111001f010100061a024b53535009181c"
    b = "686974207468652062756c6c277320657965"

    p = binascii.a2b_hex(a)
    q = binascii.a2b_hex(b)


    print(binascii.hexlify(xor(p, q)).decode())


