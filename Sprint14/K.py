def merge(arr, lf, mid, rg):
    new = []
    a = arr[:mid]
    b = arr[mid:]
    N = len(a)
    M = len(b)
    i = 0
    j = 0
    while i < N and j < M:
        if a[i] < b[j]:
            new.append(a[i])
            i += 1
        else:
            new.append(b[j])
            j += 1
    new += a[i:] + b[j:]
    return new


def merge_sort(arr, lf, rg):
    if len(arr[lf:rg]) < 2:
        return arr[lf:rg]
    mid = (lf + rg) // 2
    merge_sort(arr, lf, mid)
    merge_sort(arr, mid, rg)
    arr[lf:rg] = merge(arr, lf, mid, rg)
