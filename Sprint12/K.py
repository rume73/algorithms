# 52066474
def Form(X, list, K):
    list = list[::-1]
    K = K[::-1]
    size = max(len(K), len(list))
    K += [0]*(size-len(K))
    list += [0]*(size-len(list))
    list = [int(item) for item in list]
    Final = []
    k = 0
    for i in zip(list, K):
        s = i[0] + i[1] + k
        if s >= 10:
            k = 1
            s %= 10
        else:
            k = 0
        Final.append(int(s))
    if k == 1:
        Final.append(k)
    return Final[::-1]


if __name__ == '__main__':
    print(*Form(input(), input().split(),
          [int(x) for x in ''.join(input().split())]))
