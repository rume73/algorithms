# 51876519
def Palindrom(k):
    if k <= 3:
        if x[0] == x[-1]:
            return True
        else:
            return False
    for i in range(int(len(x) / 2)):
        if x[i] == x[k-1]:
            k -= 1
        else:
            return False
    return True


x = input().lower()
x = x.replace(' ', '')
x = x.replace(':', '')
x = x.replace(',', '')
x = x.replace('.', '')
x = x.replace('-', '')
x = x.replace('!', '')
x = x.replace('?', '')
x = list(x)
k = len(x)
print(Palindrom(k))
