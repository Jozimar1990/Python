def fat(a):
    res = 1
    for i in range(1,a+1):
        res *= i
    return res


def fat2(a):
    a *= a-1
    return fat(a)