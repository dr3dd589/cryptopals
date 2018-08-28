
def scr_plntxt(s):
    list_of_ascii_char = filter(lambda x: 'a'<=x<='z' or 'A'<=x<='Z', s)
    return float(len(list_of_ascii_char))/len(s)



def xor_with_single_byte(s):
    arr = []
    for i in range(256):
        chrs = [chr(ord(a) ^ i) for a in s]
        arr.append([scr_plntxt(chrs), ''.join(chrs)])

    return max(arr, key=lambda x: x[0])

for line in  open('s1c4.txt', 'r'):
    a = line.rstrip()
    cipher = a.decode('hex')


result = []
if __name__=='__main__':
    for line in open('s1c4.txt', 'r'):
        a = line.rstrip()
        cipher = a.decode('hex')
        result.append(xor_with_single_byte(cipher))

flag_arr= []
result.remove(max(result))
flag_arr +=  max(result, key=lambda x: x[0])
a = flag_arr[1]
flag = ""
for i in range(len(a)):
    if ord(a[i]) in range(65, 122):
        flag += a[i]
    else:
        flag += " "

print flag






