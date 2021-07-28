# 51876170
n = int(input())
x = [str(i) for i in input().split()]
k = 0
m = 0
for j in range(len(x)):
    if len(list(x[j])) > k:
        k = len(list(x[j]))
        m = j

print(x[m])
print(k)
