'''
Convert hex to base64

Rules: Always operate on raw bytes, never on encoded strings. Only use hex and base64 for pretty-printing.

Input: 49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
Ouput: SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
'''

BASE64_MAPPINGS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"


def to_base64(bytes):
    if len(bytes) % 2 != 0:
        print('Bytes is malformed')
        exit(1)

    binary = ''
    for i in range(0, len(bytes), 2):
        _hex = bytes[i : i+2]
        _int = int(_hex, 16)
        _char = chr(_int)
        _bin = bin(_int)[2:].rjust(8, '0')

        binary += str(_bin)


    base64 = ''
    for i in range(0, len(binary), 6):
        _bin = binary[i : i+6]
        _bin_len = len(_bin)
        padding = ''

        if _bin_len != 6:
            _bin = _bin.ljust(6, '0')
            padding_count = 6 - _bin_len
            padding = '=' * (padding_count // 2)

        _int = int(_bin, 2)
        base64 += BASE64_MAPPINGS[_int]
        base64 += padding

    return base64


def test(input, expected):
    actual = to_base64(input)

    if expected != actual:
        print('[mismatch] {} != {}'.format(expected, actual))


test(b'49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d','SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t')

test(b'4d616e2069732064697374696e677569736865642c206e6f74206f6e6c792062792068697320726561736f6e2c2062757420627920746869732073696e67756c61722070617373696f6e2066726f6d206f7468657220616e696d616c732c2077686963682069732061206c757374206f6620746865206d696e642c20746861742062792061207065727365766572616e6365206f662064656c6967687420696e2074686520636f6e74696e75656420616e6420696e6465666174696761626c652067656e65726174696f6e206f66206b6e6f776c656467652c2065786365656473207468652073686f727420766568656d656e6365206f6620616e79206361726e616c20706c6561737572652e', 'TWFuIGlzIGRpc3Rpbmd1aXNoZWQsIG5vdCBvbmx5IGJ5IGhpcyByZWFzb24sIGJ1dCBieSB0aGlzIHNpbmd1bGFyIHBhc3Npb24gZnJvbSBvdGhlciBhbmltYWxzLCB3aGljaCBpcyBhIGx1c3Qgb2YgdGhlIG1pbmQsIHRoYXQgYnkgYSBwZXJzZXZlcmFuY2Ugb2YgZGVsaWdodCBpbiB0aGUgY29udGludWVkIGFuZCBpbmRlZmF0aWdhYmxlIGdlbmVyYXRpb24gb2Yga25vd2xlZGdlLCBleGNlZWRzIHRoZSBzaG9ydCB2ZWhlbWVuY2Ugb2YgYW55IGNhcm5hbCBwbGVhc3VyZS4=')
test(b'4d', 'TQ==')
test(b'4d61', 'TWE=')
