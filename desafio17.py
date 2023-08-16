#Peça ao usuário para digitar a sua idade. Se a idade for menor que 13, imprima "Você é uma criança".
#Se a idade estiver entre 13 e 19, imprima "Você é um adolescente".
#Se a idade for 20 ou mais, imprima "Você é um adulto".

idade = int(input("Informe a sua idade: "))

print("Você é uma criança") if idade < 13 else (
    print("Você é um adolescente") if 13 <= idade < 20 else print("Você é um adulto"))