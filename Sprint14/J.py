# 52198150
import copy


def bubble_sort(n, array):
    for j in range(n-1):
        flag = False
        for i in range(n-1-j):
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                flag = True
        if flag is False:
            return array
        print(*array)
    return array


if __name__ == '__main__':
    n = int(input())
    arr = [int(i) for i in input().split()]
    sort_arr = copy.deepcopy(arr)
    sort_arr = bubble_sort(n, sort_arr)
    if arr == sort_arr:
        print(*arr)
