# 51873415
def Sosedi(An, Am):
    if m == 1 and n == 1:
        return ''
    elif n == 1:
        if Am == 0:
            return [x[An][Am + 1]]
        elif Am == m-1:
            return [x[An][Am - 1]]
        else:
            return [x[An][Am + 1], x[An][Am - 1]]

    elif m == 1:
        if An == 0:
            return [x[An + 1][Am]]
        elif An == n - 1:
            return [x[An - 1][Am]]
        else:
            return [x[An + 1][Am], x[An - 1][Am]]

    else:
        if An == 0 and Am == 0:
            return [x[An + 1][Am], x[An][Am + 1]]
        elif An == n-1 and Am == 0:
            return [x[An - 1][Am], x[An][Am + 1]]
        elif An == 0 and Am == m - 1:
            return [x[An][Am - 1], x[An + 1][Am]]
        elif An == n - 1 and Am == m - 1:
            return [x[An - 1][Am], x[An][Am - 1]]

        elif An == 0 and Am >= 0 and Am <= m - 1:
            return [x[An][Am + 1], x[An][Am - 1], x[An + 1][Am]]
        elif Am == 0 and An >= 0 and An <= n - 1:
            return [x[An + 1][Am], x[An - 1][Am], x[An][Am + 1]]
        elif An == n - 1 and Am >= 0 and Am <= m - 1:
            return [x[An - 1][Am], x[An][Am + 1], x[An][Am - 1]]
        elif Am == m - 1 and An >= 0 and An <= n - 1:
            return [x[An + 1][Am], x[An][Am - 1], x[An - 1][Am]]
        else:
            return [x[An - 1][Am], x[An + 1][Am], x[An][Am + 1], x[An][Am - 1]]


n = int(input())
m = int(input())
x = []
for i in range(n):
    x.append([int(j) for j in input().split()])
An = int(input())
Am = int(input())
print(*sorted(Sosedi(An, Am)))
