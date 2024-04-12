s = ''
sum = 0
for i in range(1, 10):
    s += str(i)
    sum = int(s) * 8 + i
    print(s, '* 8 +', i, '=', sum)
s = ''
sum = 0
for i in range(1, 10):
    s += str(i)
    sum = int(s) * 9 + i + 1
    print(s, '* 9 +', i + 1, '=', sum)
s = ''
sum = 0
for i in range(1, 10):
    s += '1'
    sum = int(s) ** 2
    print(s, '*', s, '=', sum)