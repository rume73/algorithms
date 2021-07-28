# 52205000
def flowerbed(array):
    array.sort()
    result = [array[0]]
    for item in array[1:]:
        if item[0] > result[-1][1]:
            result.append(item)
        else:
            if result[-1][1] < item[1]:
                result[-1][1] = item[1]
    return result


if __name__ == '__main__':
    n = int(input())
    fields = flowerbed([list(map(int, input().split())) for _ in range(n)])

    for item in flowerbed(fields):
        print(*item)
