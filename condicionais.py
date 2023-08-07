import datetime

tempo = int(input('Quanto tempo tem seu carro? '))

if tempo <= 3:
    print('Carro Novo')
else:
    print('Carro Velho')


idade = int(input('\nQual sua idade? '))
print('Maior de idade'if idade >=18 else 'Menor de idade')


nome = str(input('\nDigite seu nome: '))
n1 = float(input('Digite sua primeiro nota {}: '.format(nome)))
n2 = float(input('Digite sua segunda nota {}: '.format(nome)))
media = (n1+n2)/2
if media >= 7:
    print('Você foi aprovado!\n')
else:
    print('Infelizmente, terá que ir para final.\n')


#Escreve um programa que faça o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o
#número escolhido pelo compútador
#O programa deve escrever na tela se o usuário ganhou ou perdeu

import random
import emoji
import time
computador = random.randint(0, 5)  #random gera um número aleatório, randint(a,b) gera um número aleatório entre a e b, sendo a num min e b num max
print('-=-'*12)
print('😎 Bem Vindo Ao Jogo Da Adivinhação! 😎')
print('-=-'*12)
print('Vou pensar em um número entre 0 e 5, tente adivinhar!')
n = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
time.sleep(2)   #Vai esperar 2 segundos para dar a resposta
if n == computador:
    print('Ganhou!')
else:
    print('Perdeu! Eu pensei no número {} e não no número {}\n'.format(computador, n))


#Escreve um programa que leia a velocidaded de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
#A multa vai custar 7.0 por cada km acima do permitido.
print('-=-'*10)
print('Radar Eletrônico')
print('-=-'*10)
vel = float(input('\nQual a velocidade do seu carro? '))
if vel > 80:
    print('MULTADO! Você ultrapassou o limite permitido.')
    limite = 80
    multa = (vel - limite) * 7
    print('Valor da multa: {:.2f} reais'.format(multa))
else:
    print('Tenha um bom dia e digija com segurança!')

#Crie um programa que leia um número inteiro e mostre se ele é par ou impar

num = int(input('\nDigite um número: '))
if num % 2 == 0:
    print('O número {} é par!'.format(num))
else:
    print('O número {} é impar!'.format(num))

#Crie um programa que pergunte a distancia de um viagem em km. Calcule o preço da passagem, cobrando R$0,50 por km para viajens de até
#200km e R$0,45 para viajens mais longas.

distancia = float(input('\nQual a distãncia total da viajem em km? '))
print('Você está prestes a começar uma viajem de {}km'.format(distancia))
if distancia <= 200:
    passagem = 0.50 * distancia
else:
    passagem = 0.45 * distancia
print('O preço da passagem analisando os km percorridos, será: {:.2f}'.format(passagem))


#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

import datetime
ano = int(input('\nDigite um ano especial para você, se quiser analisar o ano atual digite 0: '))
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é Bissexto!'.format(ano))
else:
    print('O ano {} não é Bissexto!'.format(ano))


#Faça um programa que leia três números e mostre qual é o maior e qual o menor

n1 = int(input('\nDigite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))

if n1 > n2 and n1 > n3:
    print('O número {} é o maior'.format(n1))
if n2 > n3 and n2 > n1:
    print('O número {} é o maior'.format(n2))
if n3 > n2 and n3 > n1:
    print('O número {} é o maior'.format(n3))

if n1 < n2 and n1 < n3:
    print('O número {} é o menor'.format(n1))
if n2 < n3 and n2 < n1:
    print('O número {} é o menor'.format(n2))
if n3 < n2 and n3 < n1:
    print('O número {} é o menor'.format(n3))

#Faça um programa que pergunte o valor de seu salário e calcule o valor de seu aumento.
#Para salários superiores a 1.250,00 o aumento é de 10%
#Para inferiores ou iguais o aumento é de 15%

salario = float(input('\nQual o valor de seu salário atual? '))
if salario <= 1250:
    aumento = salario * (15 / 100)
    salarioAtual = salario + aumento
else:
    aumento = salario * (10 / 100)
    salarioAtual = salario + aumento

print('O seu salário Atual ficará {} após o aumento de {} reais'.format(salarioAtual, aumento))


#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triangulo.

reta1 = float(input('\nComprimento da primeira reta: '))
reta2 = float(input('Comprimento da segunda reta: '))
reta3 = float(input('Comprimento da terceira reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta3 and reta3 < reta2 + reta1:
    print('As retas acima PODEM FORMAR um triângulo!')
else:
    print('As retas acima NÃO PODEM FORMAR um triãngulo!')