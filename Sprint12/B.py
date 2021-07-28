# 51806079
def Game(a, b, c):
    if (a % 2 == 0 and b % 2 == 0 and c % 2 == 0
            or a % 2 != 0 and b % 2 != 0 and c % 2 != 0):
        return 'WIN'
    else:
        return 'FAIL'


a, b, c = map(int, input().split())
print(f'{Game(a, b, c)}')
