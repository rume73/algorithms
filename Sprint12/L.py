# 52073600
def String(word1, word2):
    word1 = sorted(list(word1))
    word2 = sorted(list(word2))
    k = 0
    extra_symbols = []
    while len(word1) != len(word2):
        if len(word1) < len(word2):
            for x, y in zip(word1, word2):
                if x != y:
                    word1.insert(k, '0')
                    break
                k += 1
            if len(word1) != len(word2):
                word1.append('0')
        else:
            for x, y in zip(word1, word2):
                if x != y:
                    word2.insert(k, '0')
                    break
                k += 1
            if len(word1) != len(word2):
                word2.append('0')
    for x, y in zip(word1, word2):
        if x == '0':
            extra_symbols.append(y)
        if y == '0':
            extra_symbols.append(x)
    return extra_symbols


if __name__ == '__main__':
    print(*String(input(), input()))
