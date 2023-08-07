#Faça um programa que leia um número inteiro e apresente seu sucessor e antecessor

num = int(input('Digite um número: '))
sucessor = num + 1
antecessor = num - 1
print('O número {} tem como sucessor o número {} e como antecessor o número {}.\n'.format(num, sucessor, antecessor))


#Faça um programa que leia um número mostre o seu dobro, o triplo e sua raiz quadrada

num1 = int(input('Digite um número: '))
dobro = num1*2
triplo = num1*3
raiz = pow(num1, (1/2))
#Outra forma de calcular raiz quadrada : raiz = num1 ** (1/2)
print('O dobro de {} é: {} \nO triplo é: {} \nA raiz quadrada é: {:.2f}\n'.format(num1, dobro, triplo, raiz))


#Faça um programa que leia as notas de um aluno e mostre sua média

nota1 = float(input('Qual sua primeira nota? '))
nota2 = float(input('Qual sua segunda nota? '))
media = (nota1 + nota2)/2

print('As suas notas foram {} e {} e sua média ficou: {:.2f}\n'.format(nota1, nota2, media))


#Escreva um programa que leia um valor em metros e exiba ele convertido em centimetros e milimetros

metros = int(input('Digite um valor em metros: '))
centimetros = metros*100
mili = centimetros*10

print('Análisando o valor {}m, transformando em centimetros fica: {}cm e em milimetros fica: {}mm\n'.format(metros, centimetros, mili))


#Faça um programa que leia um número inteiro e mostre na tela a sua tabuada

numero = int(input('Digite um número: '))
t = "TABUADA"
print('{:-^50}'.format(t))
n1 = numero * 1
n2 = numero * 2
n3 = numero * 3
n4 = numero * 4
n5 = numero * 5
n6 = numero * 6
n7 = numero * 7
n8 = numero * 8
n9 = numero * 9
n10 = numero * 10

print(' {}*1 = {}\n {}*2 = {}\n {}*3 = {}\n {}*4 = {}\n {}*5 = {}\n {}*6 = {}\n {}*7 = {}\n {}*8 = {}\n {}*9 = {}\n {}*10 = {}\n'.format(numero, n1, numero, n2, numero, n3, numero, n4, numero, n5, numero, n6, numero, n7, numero, n8, numero, n9, numero, n10))


#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar. Considere US$1.00 = R$3.27

nome = input('Qual seu nome? ')
carteira = float(input('Quanto dinheiro você tem na carteira {}? '.format(nome)))
dolar = carteira / 3.27

print('{} você poderá comprar {:.2f} doláres.\n'.format(nome, dolar))

#faça um programa que leia a largura e altura de uma parede em metros. calcule a sua área e a quntidade de tinta necessaria para pintá-la sabendo que cada litro de tinta pinta uma área de 2m²

largura = float(input('\nQual a largura da parede em metros? '))
altura = float(input('Qual a altura da parede em metros? '))
area = largura * altura
tinta = area / 2

print('Sabendo que a largura da parede é {} e a altura {}, a quantidade de tinta a ser utilizada é: {}l\n'.format(largura, altura, tinta))

#Faça um programa que leia o preço de um produto e mostre seu novo p reço com 5% de desconto

preco = float(input('\nDigite o preço do produto: '))
novoPreco = preco - (preco * 5 / 100)
print('O novo preço do produto com o desconto é: {:.2f}'.format(novoPreco))

#Faça um programa que leia o salario de um funcionario e mostre o novo salario com 15% de aumento

n = input('\nQual seu nome? ')
salario = float(input('Digite o seu salário {}: '.format(n)))
novosal = salario + (salario * 15 / 100)
print('O novo salário com o aumento é: {:.2f}'.format(novosal))
