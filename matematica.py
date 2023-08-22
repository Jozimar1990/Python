#https://pense-python.caravela.club/11-dicionarios/07-variaveis-globais.html


def fat(a):
    res = 1
    for i in range(1,a+1):
        res *= i
    return res

def fat2(a):
    return 1 if a == 0 else a * fat2(a-1)