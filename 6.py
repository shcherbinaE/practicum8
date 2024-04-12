for i in range(1,11):
    s = ''
    for j in range(1,11 - i):
        s += ' '
    for j in range(10 - i,10):
        s += '*'
    print(s)