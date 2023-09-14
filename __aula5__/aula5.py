num = 5
num2 = 7
valor = (num + num2)/2
index = 0

if valor > num and valor < num2: print("verdadeiro")
else: print("falso")

if num < valor < num2: print("verdadeiro")
else: print("falso")

print("verdadeiro") if num < valor < num2 else print("falso")

frase = input("informe o seu nome e a sua idade: ")
frase = frase.split()
for frases in frase:
    if frases.isnumeric() == True: 
        index = frase.index(frases)
print(f'você tem {frase[index]} anos') 
 