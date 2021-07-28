# 52200637
from functools import cmp_to_key


def my_cmp(x, y):
    if x+y > y+x:
        return -1
    elif x+y == y+x:
        return 0
    else:
        return 1


if __name__ == '__main__':
    input()
    arr = input().split()
    arr.sort(key=cmp_to_key(my_cmp))
    print(*arr, sep='')
