frase = 'Tudo posso nAquele que me fortalece'
x = slice(0, 5)
print(frase.index('o'))
print(frase[1:6])
print(frase[x])

frase2 = 'O Jozimar Lima é um excelente programador'

frase2 = frase2.split()
nome = frase2[1]
sobrenome = frase2[2]
profissao = frase2[6]

text = f'''
    o {nome} {sobrenome} é um excelente {profissao}

'''

print(f'''
      Me chamo {nome} {sobrenome}
      E minha profissão é {profissao}
      ''')

print(text)