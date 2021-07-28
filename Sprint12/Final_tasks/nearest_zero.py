# 52062151
def nearest_zero(house_numbers, zero='0') -> list:
    zeros = [pos for pos, number in enumerate(house_numbers)
             if house_numbers[pos] == zero]
    distances = [0] * len(house_numbers)
    for left, right in zip(zeros[:-1], zeros[1:]):
        distances[left + 1:right] = [
            min(house - left, right - house)
            for house in range(left + 1, right)
            ]
    first = zeros[0]
    distances[:first] = [first - house for house in range(first)]
    last = zeros[-1]
    distances[last + 1:] = [
        house - last for house in range(last + 1, len(house_numbers))
        ]
    return distances


if __name__ == '__main__':
    input()
    print(*nearest_zero(input().split()))
