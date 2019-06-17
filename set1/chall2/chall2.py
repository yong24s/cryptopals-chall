'''
Fixed XOR

Write a function that takes two equal-length buffers and produces their XOR combination.

Input 1: 1c0111001f010100061a024b53535009181c
Input 2: 686974207468652062756c6c277320657965
Output:  746865206b696420646f6e277420706c6179

'''

def xor(a, b):
    if len(a) != len(b):
        print('inputs size mismatch')
        error(1)

    output = ''
    for i in range(0, len(a), 2):
        hex_a = a[i : i + 2]
        hex_b = b[i : i + 2]

        j = int(hex_a, 16) ^ int(hex_b, 16)
        output += hex(j)[2:]

    return output

expected = '746865206b696420646f6e277420706c6179'
actual = xor(b'1c0111001f010100061a024b53535009181c', b'686974207468652062756c6c277320657965')

if expected != actual:
    print('mismatch')
