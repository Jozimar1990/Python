#quero que você crie um loop que imprima os números de 1 a 10, mas pare de imprimir assim que chegar a 5 usando o comando "break".
#Em seguida, crie um segundo loop que imprima os números 1 a 10, mas que pule a impressão do número 5, usando o comando "continue".
for i in range(1, 11):
    if i == 5:
        break
    for j in range(1, 11):
        if j == 5:
            continue
        print(f'{i} {j}')