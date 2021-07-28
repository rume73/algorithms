# 52205486
def cloakroom(n, arr):
    return arr.count('0') * '0' + arr.count('1') * '1' + arr.count('2') * '2'


if __name__ == '__main__':
    print(*cloakroom(input(), input().split()))
