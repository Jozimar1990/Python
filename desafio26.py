#Crie uma função que calcule a potência de um número.
#A função deve aceitar dois argumentos: a base e o expoente.
#No entanto, se o exponte não for fornecido, ele deve assumir o valor padrão de 2.

def quadrado(a, b = 2):
    return   a**b

print(quadrado(2,5))
print(quadrado(2))

def soma(*num):
    resultado = 0
    for n in num:
        resultado  += n
    return resultado

print(soma(1, 2, 3, 4))

def cadastro(*dados):
    return dados


nome = 'Jozimar'
sobrenome = 'Sarmento'
idade = 33

print(cadastro(nome, sobrenome, idade))

def cadast(*dados):
    return dados

dado = {
    nome: "jozimar",
    sobrenome: 'Sarmento',
    idade: 33
}

print(cadast(dado))

def cadast(**dados):
    return dados

view = 'nome'
sobreview = 'sarmento'
old  = 33
#print(cadast(view, sobreview, old)) #essa linha não funciona
print(cadast(nome = 'Jozimar', sobrenome = 'Sarmento', idade = 33))

import matematica as f
print(f.fat(5))