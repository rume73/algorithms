# 52164219
def generate(n, open, close, cur):
    if len(cur) == 2*n:
        print(cur)
        return
    if open < n:
        generate(n, open+1, close, cur+'(')
    if close < open:
        generate(n, open, close+1, cur+')')


if __name__ == '__main__':
    generate(int(input()), 0, 0, '')
