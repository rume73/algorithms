# 52168257
def phone_buttons(prefix, sequence, cur_button_in_sequence, n, i):
    if n == 0:
        sequence.append(prefix)
        i = 0
    for j in range(11):
        if n == j:
            for ch in cur_button_in_sequence[i]:
                phone_buttons(prefix + ch, sequence,
                              cur_button_in_sequence, n-1, i+1)
    return sequence


if __name__ == '__main__':
    prefix = ''
    number = [*map(int, input())]
    buttons = {
        2: 'abc',
        3: 'def',
        4: 'ghi',
        5: 'jkl',
        6: 'mno',
        7: 'pqrs',
        8: 'tuv',
        9: 'wxyz'}
    cur_button_in_sequence = []
    for i in range(len(number)):
        cur_button_in_sequence.append(buttons[number[i]])
    n = len(cur_button_in_sequence)
    result = phone_buttons('', [], cur_button_in_sequence, n, 0)
    print(*result)
