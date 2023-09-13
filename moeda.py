#Crie um módulo chamado moeda.py que tenha as funções
#incorporadas, aumentar(), diminuir(), dobro(), e metade().
#Faça também um programa que importa esse módulo e use algumas funções e crie o módulo teste.py

def aumentar(preco, taxa):
    return preco + (preco * taxa/100)

def diminuir(preco, taxa):
    return preco - (preco * taxa/100)

def dobro(preco):
    return preco * 2

def metade(preco):
    return preco/2