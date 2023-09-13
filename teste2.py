import moeda as md
preco = 180.00
taxa = 10
print(f'O aumento do valor {preco} é de {md.aumentar(preco, taxa)}')
print(f'O decrescimo do valor {preco} é de {md.diminuir(preco, taxa)}')
print(f'O dobro do valor {preco} é de {md.dobro(preco)}')
print(f'A metade do valor {preco} é de {md.metade(preco)}')