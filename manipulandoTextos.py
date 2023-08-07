#cadeia de caracteres = uma frase = string

   #FATIAMENTO = pegar pedaços de uma cadeia de caracteres

   #ANALISE = analisar com que letra comeca, com qual termina, quantidade de letras...
#EX: frase = 'Curso em Video Python'

#len(frase) = comprimento da frase

#frase.count('o') = contar quantos o tem na minha frase

#frase.find(deo) = find=encontrar, nesse caso é quantas vezes encontrou deo na frase

#frase.find('Android') = se coloca no find uma string q não existe ele retorna a posição -1, insinuando que n foi encontrado

#'Curso' in frase = dentro de frase tem a string Curso?, vai retornar truw

   #TRANSFORMAÇÃO =

#frase.replace('Python', 'Android') = replace=reposicionar, nesse caso substitui Python por Android

#frase.upper() = upper=paracima, ficando em maiusculas

#frase.lower() = passa para minusculo

#frase.capitalize() = joga todos caracteres para minusculo e só a primeira letra em maiuscula

#frase.title() = analisa quantas palavras tem e faz o capitalize de palavra em palavra

#frase.strip() = remove todos os espaços inuteis do começo e final da frase

#frase.rstrip() = remove somento o últimos espaços, no caso da direita

#frase.lstrip() = remove somento o primeiros espaços, no caso da esquerda

   #DIVISAO =

#frase.split() = onde tem espaço na frase cria uma divisão

   #JUNÇÃO =

#'-'.join(frase) = junta todos os elementos de frase e usa o separador -

#teste09

frase = 'Curso em Video Python'
print(frase)
print(frase[3])  #mostra a letra da 3 posição
print(frase[:13])  #mostra a frase do inicio até a posição 13
print(frase[13:])   #mostra a frase da posição 13 até o final
print(frase[3:13])  #mostra da posição 3 até a posição 13
print(frase.count('o'))  #conta quantos o tem na frase
print(len(frase))  #comprimento frase
print(frase.upper())  #deixa tudo em maiusculo
print(frase.lower())  #deixa tudo em minusculo
print(frase.capitalize())  #deixa a primeira letra da frase maiuscula
print(frase.title())  #começo de toda alavra em maiuscula
print('-'.join(frase.split()))  #coloca - em cada espaço


#01: crie um programa que leia o nome completo de uma pessoa e
# apareça na tela o nome com todas as letras maiusculas
# o nome com todas as letras minusculas
# quantas letras ao todo
# quantas letras tem o primeiro nome

nome = str(input('\nDigite seu nome completo: ')).strip()
print('O seu nome em maiúisculo é {}'.format(nome.upper()))
print('O seu nome em maiúisculo é {}'.format(nome.lower()))
print('O seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))  #quantidade de letras menos os espaços
print('O seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print(separa)
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], nome.find(' ')))

#02: faça um programa que leia um numero de 0 a 9999 e mostre na
# tela cada um dos digitos separados.
# EX: digite um número: 1834
#unidade: 4
#dezena:3
#centena:8
#milhar:1

num = int(input('\nDigite um número: '))
print(num)
#n = str(num)          #Só funciona se o numero tiver 4 digitos
#print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(n[3], n[2], n[1], n[0]))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {} \nDezena: {} \nCentena: {} \nMilhar: {}'.format(u, d, c, m))

#03: crie um programa que leia o nome de uma cidade e diga se
# ela começa ou não com o nome "SANTO".

cidade = str(input('\nEm que cidade você nasceu? ')).strip()
print(cidade[0:5].upper() == 'SANTO')

#04: crie um programa que leia o nome de uma pessoa e diga se
# ela tem "SILVA" no nome".

name = str(input('\nDigite seu nome completo: ')).strip().upper()
nn = 'SILVA' in name
print(nn)

#05: programa que leia um frase e mostre:
#quantas vezes aparece a letra "A"
#em que posição aparece a primeira vez
#em que posição aparece a últims vez

f = str(input('\nDigite uma frase: ')).strip().upper()
print('A letra "A" aparece {} vezes'.format(f.count('A')))
print('A letra "A" aparece a primeira vez na posição {}'.format(f.find('A')))
print('A letra "A" aparece a última vez na posição {}'.format(f.rfind('A')))  #rfind começa a contar do lado direito

#06: programa que lê o nome completo de uma pessoa, mostrando em
# seguida o promeiro e o ultimo nome separadamete
#EX: Ana maria de souza
#primeiro: Ana
#ultimo: souza

name = str(input('\nDigite seu nome completo: ')).title().strip()
n = name.split()
print('Primeiro nome: {}'.format(n[0]))
print('Último nome: {}'.format(n[len(n)-1]))
