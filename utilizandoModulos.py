#biblioteca MATH
 #Funcionalidades da biblioteca math:
   #CEIL serve p arredondar um número para cima
   #FLOOR arredonda um número para baixo
   #TRUNC elimina da virgula para frente de um número float
   #POW potencia
   #SQRT calcula raiz quadrada
   #FACTORIAL calcular fatorial
        #import math (importa todas funcionalidades da biblioteca)
        #from math import ceil (importa só a funcionalidade ceil da biblioteca math)

import math
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
print('A raiz de {} é {}.'.format(num, raiz))
print('A raiz de {} é {}.'.format(num, math.ceil(raiz)))   #Além de trazer o resultado da raiz, ele será arredondado para cima

import emoji
print(emoji.emojize('\nOlá Mundo 😎🌎'))   #Para add emoji vai nos docs do python.org e pesquisa emoji, vai em baixo em pesquisar emojis e copia o ink de qual quiser

#Crie um programa que leia um numero real pelo teclado e mostre na
# tela a sua porção inteira
#EX: num = 6.123 ---> num = 6

n = float(input('\nDigite um número: '))
print('O número foi: {}, e ele inteiro é: {}'.format(n, math.trunc(n)))


#faca um programa que leia o comprimento do cateto oposto e do cateto
#adjacente de um triangulo rtangulo. Calcule e mostre o comprimento da
#hipotenusa
#o quadrado da hipotenusa e igual a soma do quadrado dos catetos

co = int(input('\nQual o comprimento do cateto oposto? '))
ca = int(input('Qual o comprimento do cateto adjacente? '))
h2 = math.pow(co, 2) + pow(ca, 2)
h = math.sqrt(h2)
#hi = math.hypot(co, ca)  Outra forma de calcular a hipotenusa
print('Teorema: o quadrado da hipotenusa é igual a soma do quadrado dos catetos. \n Cateto Oposto: {}\n Cateto Adjacente: {}\n Hipotenusa: {}'.format(co, ca, h))

# faca um programa que leia um angulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse angulo.

angulo = int(input('\nDigite um ângulo: '))
seno = math.sin(math.radians(angulo))  #É necessário converter de graus para radiano
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O angulo {}° tem o seno de {:.2f}'.format(angulo, seno))
print('O angulo {}° tem o cosseno de {:.2f}'.format(angulo, cosseno))
print('O angulo {}° tem a tangente de {:.2f}'.format(angulo, tangente))


#um professor quer sortear um dos seus quatro alunos para apagar o quadro. faca um programa que ajude ele lendo o nome deles e escrevendo o nome escolhido
import random
n1 = str(input("\nDigite o nome do primeiro aluno: "))
n2 = str(input("Digite o nome do segundo aluno: "))
n3 = str(input("Digite o nome do terceiro aluno: "))
n4 = str(input("Digite o nome do quarto aluno: "))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)            #o random choice faz uma escolha entre os elementos da lista

print("O aluno escolhido foi {}".format(escolhido))

#o mesmo professor quer sortear a ordem de apresentação de trabalho dos
#alunos. Faça um programa que leia o nome dos quatro alunos e mostre a
# ordem sorteada.

np = str(input("\nPrimeiro aluno: "))
ns = str(input("Segundo aluno: "))
nt = str(input("Terceiro aluno: "))
nq = str(input("Quarto aluno: "))
lista = [np, ns, nt, nq]
sorteio = random.shuffle(lista)    #shuffle embaralha a lista

print("A ordem de apresentação será: \n")
print(lista)


#Faça um programa em python que abra e reproduza um audio de um
# arquivo em mp3

import pygame
pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()

