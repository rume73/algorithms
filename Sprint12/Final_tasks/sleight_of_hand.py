# 52061871
sleight_of_hand = (lambda
                   fingers,
                   field,
                   hands=2,
                   digits='123456789':
                   sum(
                       0 < field.count(number) <= fingers*hands
                       for number in digits
                       )
                   )


if __name__ == '__main__':
    print(sleight_of_hand(int(input()),
                          input() + input() + input() + input()))
