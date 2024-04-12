x = int(input())
sum = 1
s = '1'
print(s)
for i in range(2, x + 1):
    s += ' + ' + str(i)
    sum += i
    print(s, '=', sum)
