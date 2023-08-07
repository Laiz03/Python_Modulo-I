nome = input('Qual seu nome? ')
print('Prazer em te conhecer {:20}!'.format(nome)) #Deixa o nome digitado em um espaco tamanho 20

print('Prazer em te conhecer {:>20}!'.format(nome)) #Deixa o nome digitado no final do espaço tam 20

print('Prazer em te conhecer {:<20}!'.format(nome)) #Deixa o nome digitado no começo do espaço tam 20

print('Prazer em te conhecer {:^20}!'.format(nome)) #Deixa o nome digitado no meio do espaço tam 20

print('Prazer em te conhecer {:=^20}!'.format(nome)) #Deixa o nome digitado no meio do espaço tam 20