import string

with open("quack.txt", "rb")as f:
    data = f.read().decode()
    
    res = ''
    for c in data:
        if c == '-':
            res += '1'
        if c == '.':
            res += '0'

    print(res)
    print(len(res))