a = 5; b = 2
soma = a+b
subtracao = a-b
multiplicacao = a*b
divisao = a/b
divisaoInteira  = a//b
exponenciacao = a**b
modulo = a%b
print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(divisaoInteira)
print(exponenciacao)
print(modulo)

soma = a+b
soma2 = a+a
velocidade = 50 
print('Acima da velocidade permitida\nFavor, diminua sua velocidade') if (velocidade >= 100) else print('Continue assim') if (velocidade <= 60) else print('Favor, dirigir acima de 80Km/h') 

frase = "velocidade do carro ultrapassou 60 KM/h"
frase = frase.split()
print(frase.index('ultrapassou'))

print("Você está no limite de velocidade") if (int(frase[frase.index('ultrapassou')+1]) <= 60) else print('Cuidado, sua vida importa')