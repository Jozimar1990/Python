
carros = ["BMW X6","Honda Civic","BMW I5","Ford Fusion","BMW I8"]
car = input("Informe a marca e o modelo (nesta ordem) o qual deseja pesquisar: ")
cont = 0
for carro in carros:
    if car.upper() == carro.upper():
        cont = cont + 1
print("Este carro está disponível") if cont != 0 else print("Desculpe, este carro não está disponível no momento")