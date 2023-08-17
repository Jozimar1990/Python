#Crie uma função que calcule a potência de um número.
#A função deve aceitar dois argumentos: a base e o expoente.
#No entanto, se o exponte não for fornecido, ele deve assumir o valor padrão de 2.

def quadrado(a, b = 2):
    return   a**b

print(quadrado(2,5))
print(quadrado(2))