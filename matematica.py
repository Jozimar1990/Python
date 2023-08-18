#https://pense-python.caravela.club/11-dicionarios/07-variaveis-globais.html


def fat(a):
    res = 1
    for i in range(1,a+1):
        res *= i
    return res
global fator
fator = 1
def fat2(a):
    b = a
    def fatorar(b):
        global fator
        fator *= b-1
        return fator if b == 1 else fatorar(b) 
    
    return fatorar(a)