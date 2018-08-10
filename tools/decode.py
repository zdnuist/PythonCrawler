def decode(s):
    return ''.join([chr(i) for i in [int(b, 2) for b in s.split(' ')]])