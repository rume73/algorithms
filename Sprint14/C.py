# 52204976
def is_subsequence(part, full):
    part = list(part)
    count = 0
    if len(part) == 0:
        return True
    cur_letter = part[count]
    for letter in full:
        if letter == cur_letter:
            count += 1
            if count == len(part):
                return True
            cur_letter = part[count]
    return False


if __name__ == '__main__':
    print(is_subsequence(input(), input()))
