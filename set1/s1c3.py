
cipher = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'

def scr_plntxt(s):
    list_of_ascii_char = filter(lambda x: 'a'<=x<='z' or 'A'<=x<='Z', s)
    return float(len(list_of_ascii_char))/len(s)

def xor_with_single_byte(s):
    arr = []
    for i in range(256):
        chrs = [chr(ord(s) ^ i) for s in cipher.decode('hex')]
        arr.append([scr_plntxt(chrs), ''.join(chrs)])
    return max(arr, key=lambda a: a[0])

if __name__ == '__main__':
    print xor_with_single_byte(cipher)