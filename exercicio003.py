#Receba algo pelo teclado e mostre na tela seu tipo primitivo e todas as informações possiveis sobre ele

num = input("Digite algo: ")
print('O tipo primitivo desse algo é? {}'.format(type(num)))
print('É um número? {}'.format(num.isnumeric()))
print('É uma letra ou palavra? {}'.format(num.isalpha()))
print('Está em letra miniscúla? {}'.format(num.islower()))
print('Está em letra maiúscula? {}'.format(num.isupper()))
print('É um espaço? {}'.format(num.isspace()))
print('É um número ou letra/palavra? {}'.format(num.isalnum()))
print('Está capitalizada? {}'.format(num.istitle()))  #Ou seja, em maiusculo e minisculo



