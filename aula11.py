#criar a classe
class computador:
    def __init__ (self, marca, ram, placaDeVideo):
        self.marca = marca
        self.ram = ram
        self.placaDeVideo = placaDeVideo
    
    def exibirInformacoes(self):
        print(self.marca, self.ram, self.placaDeVideo)
    
    def desligar(self):
        print("Desligando")


#Criando o objeto
computador1 = computador('Asus', '16GB', "AMD")
print(computador1.marca)

computador1.exibirInformacoes()
computador1.desligar()