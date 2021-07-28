# 52230917
def key(array):
    return [-array[1], array[2], array[0]]


def rating_table(array, left, right):
    if right - left < 1:
        return
    pivot = left
    pivot_key = key(array[pivot])
    position = right
    while pivot != position:
        if pivot < position:
            if pivot_key >= key(array[position]):
                array[pivot], array[position] = array[position], array[pivot]
                pivot, position = position, pivot + 1
            else:
                position -= 1
        else:
            if pivot_key < key(array[position]):
                array[pivot], array[position] = array[position], array[pivot]
                pivot, position = position, pivot - 1
            else:
                position += 1
    rating_table(array, left, pivot-1)
    rating_table(array, pivot+1, right)


if __name__ == '__main__':
    array = []
    lenght = int(input())
    for idx in range(lenght):
        array.append(input().split())
        array[idx][1], array[idx][2] = int(array[idx][1]), int(array[idx][2])
    rating_table(array, 0, lenght-1)
    print(*[player[0] for player in array], sep='\n')
