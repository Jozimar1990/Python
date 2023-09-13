def somar(*num, a=0):
    for n, part in zip(range(len(num)), num):
        return 1 if num.index(part) == len(num) else (n + somar(num, n))
        print(len(num))

print(somar(1, 2, 3, 4))
