#numero = input("informe um numero") or 0

#cor_cliente = input("Informe uma cor: ")
cores = ['amarelo', 'verde', 'lilás', 'azul']

#print("Tem") if cor_cliente.lower() in cores else print("não tem")

valores = [10, 20, 30, 40]
valor = [53.00, 56.00]

#duas_listas = list(zip(cores, valores, valor)) # list() junta duas listas em uma, só que depende de zip()
#print(duas_listas)
frutas = input("informe o nome das frutas separados, por vírgula").replace(" ", "").split(",") or "maçã" #replace está substituindo os espaços enquanto o split separa a string em uma list
for fruta in frutas:
    print(fruta)
print(frutas)
lista = ['uva', 'banana', 'pera', 'tomate']
tupla = ('uva', 'banana', 'pera', 'tomate')