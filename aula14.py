'''
Criar um programa que calcula a quantidade de tinta necessária para
pintar uma parede. O usuário deverá fornecer as seguintes 
informações: Rendimento, altura e largura.
O programa deve mostrar na tela a mensagem 'Você necessita de x latas de tinta
'''
from calculaTinta import calcular as c
rendimento = float(input("Informe o rendimento em (m²) da lata de tinta: "))
altura = float(input("Informe a altura da parede em (m²): "))
largura = float(input("Informe a largura da parede em (m²): "))

print(f'Você necessita de {c(rendimento, altura, largura)} latas de tinta')