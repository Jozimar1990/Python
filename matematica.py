def fat(a):
    res = 1
    for i in range(1,a+1):
        res *= i
    return res

def fat2(a):
    b = a
    def fatorar(b):
        fator *= b-1
        return fator if b == 1 else fatorar(b) 
    
    return fatorar(b)