#https://www.freecodecamp.org/portuguese/news/metodo-de-listas-append-em-python-explicacao-e-exemplos-de-como-adicionar-um-elemento-a-um-array/

palavra = 'FANTASTICO'
palavra2 = []
novaPalavra = ''
print(palavra)
for i, espaco in zip(range(len(palavra)), palavra):
    palavra2.append(espaco+" ")
    novaPalavra += palavra2[i]

palavra = novaPalavra
print('\nvariável com novo valor: ', palavra)
