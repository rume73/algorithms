# 52160726
def days_of_purchase(money, bike_cost, left, right, bikes):
    if right <= left:
        if bikes[0] is None:
            return [-1, -1]
        elif bikes[0] is not None and bikes[1] is None:
            bikes[1] = 0
            return days_of_purchase(money, bike_cost, 0, days, bikes)
        elif bikes[1] == 0:
            bikes[1] = -1
        return bikes
    mid = (left + right) // 2
    if money[mid] >= bike_cost and bikes[0] is None:
        bikes[0] = mid + 1
        return days_of_purchase(money, bike_cost, left, mid, bikes)
    elif money[mid] >= bike_cost and bikes[0] > mid:
        bikes[0] = mid + 1
        return days_of_purchase(money, bike_cost, left, mid, bikes)
    elif (money[mid] >= 2*bike_cost and bikes[0] is not None
            and bikes[1] == 0):
        bikes[1] = mid + 1
        return days_of_purchase(money, bike_cost, left, mid, bikes)
    elif money[mid] >= 2*bike_cost and bikes[1] > mid:
        bikes[1] = mid + 1
        return days_of_purchase(money, bike_cost, left, mid, bikes)
    else:
        return days_of_purchase(money, bike_cost, mid + 1, right, bikes)


if __name__ == '__main__':
    days = int(input())
    print(*days_of_purchase([int(item) for item in (input().split())],
                            int(input()),
                            left=0,
                            right=days,
                            bikes=[None]*2))
