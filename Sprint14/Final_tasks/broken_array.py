# 52231056
def broken_search(nums, target):
    border = get_max(nums)
    if target == nums[border]:
        result = border
    elif border == len(nums) - 1:
        result = binary_search(nums, target, 0, border)
    elif nums[0] <= target > nums[border + 1]:
        result = binary_search(nums, target, 0, border)
    elif target < nums[border]:
        result = binary_search(nums, target, border)
    else:
        result = -1
    return result


def get_max(arr, left=0, right=None):
    right = len(arr) - 1 if right is None else right
    index_mid_elem = (right + 1 - left) // 2 + left
    mid_elem = arr[index_mid_elem]
    if arr[left] <= mid_elem <= arr[right]:
        return right
    if arr[left] > mid_elem:
        return get_max(arr, left=left, right=index_mid_elem - 1)
    else:
        return get_max(arr, left=index_mid_elem, right=right)


def binary_search(arr, target, left=0, right=None):
    right = len(arr) - 1 if right is None else right
    if right < left:
        return -1
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(arr, target, left, mid - 1)
    else:
        return binary_search(arr, target, mid + 1, right)
