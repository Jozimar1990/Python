#Crie uma lista de frutas que inclui "maçã" três vezes e outras frutas de sua preferência.
#Use um loop para contar quantas vezes "maçã" aparece na lista e imprima o seu resultado
frutas = ['maçã', 'uva', 'tomate', 'pêra', 'maçã', 'banana', 'maçã', 'abacate']

cont = 0
for fruta in frutas:
    if fruta == 'maçã':
        cont = cont + 1
print(f'Total de {cont} maçãs')