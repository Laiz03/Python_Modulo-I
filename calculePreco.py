#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a
# quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

km = float(input('Qual a quantidade de km percorridos? '))
dias = int(input('Quantos dias o carro ficou alugado? '))
qKm = 0.15 * km
qDias = 60 * dias
total = qKm + qDias

print('O preço total do aluguel do carro foi: {:.2f}'.format(total))

