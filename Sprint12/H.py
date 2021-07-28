# 51883236
x = [*map(int, input())]
y = [*map(int, input())]
x = x[::-1]
y = y[::-1]
size = max(len(x), len(y))
x += [0]*(size - len(x))
y += [0]*(size - len(y))
f = []
k = 0
for i in zip(x, y):
    s = i[0] + i[1] + k
    k = int(s / 2)
    f.append(int(s % 2))
if k == 1:
    f.append(k)
print(''.join(map(str, f[::-1])))
