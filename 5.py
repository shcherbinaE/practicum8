a = int(input())
num = 0
for i in range(2, a):
    s = 0
    for j in range(1, int(i // 2) + 1):
        if i % j == 0:
            s += j
    if s == i:
        num += 1
print(num)