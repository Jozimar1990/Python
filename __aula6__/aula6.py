#For loop - utilizando o if else
#Enviar um email com detalhes de compra online (máximo 3 tentativas) para compras confirmadas

compraConfirmada = False 
dadosCompras = 'Compra no valor de R$ 12,50  e  entrega confirmada'
for tentativa in range(3):
    if compraConfirmada:
        print(dadosCompras)
    else:
        print("Falha na compra, tente novamente")
