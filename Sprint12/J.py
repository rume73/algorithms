# 51884408
x = int(input())
p = []
i = 2
while i * i <= x:
    while x % i == 0:
        p.append(i)
        x = int(x / i)
    i += 1
if x > 1:
    p.append(x)

print(' '.join(map(str, p)))
