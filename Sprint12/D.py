# 51875867
n = int(input())
x = [int(i) for i in input().split()]
k = 0
if n == 1:
    k += 1
else:
    if x[0] > x[1]:
        k += 1
    if x[-1] > x[-2]:
        k += 1
    for j in range(1, n - 1):
        if x[j - 1] < x[j] > x[j + 1]:
            k += 1
print(k)
