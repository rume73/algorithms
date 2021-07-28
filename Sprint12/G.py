# 51881604
x = int(input())
f = ''

while x > 0:
    f = str(x % 2) + f
    x = int(x / 2)

print(f)
