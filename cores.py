#     style;       ;background
#\033[                        m
#            ;text;
#EX: \033[0;33;44m
#ENTENDENDO MELHOR:

#STYLE=
  # 0: none, ou seja nenhum estilo
  # 1: bold, ou seja negrito
  # 4: underline, ou seja sublinhado
  # 7: negative, inverte ou seja, oq colocou para fundo vai ficar em letra e o que colocou em letra vai para fundo

#TEXT=
  # 30: branco
  # 31: vermelho
  # 32: verde
  # 33: amarelo
  # 34: azul
  # 35: roxo
  # 36: azul ciano
  # 37: cinza

#BACK=
  # 40: branco
  # 41: vermelho
  # 42: verde
  # 43: amarelo
  # 44: azul
  # 45: roxo
  # 46: azul ciano
  # 47: cinza


print('\033[1;31;43mOlá, Mundo!\033[m\n')

print('\033[7;40mMeu nome é Laíz!\033[m\n')  #Inverteu, a cor de fundo foi para a cor do texto e a cor do texto para o fundo

print('\033[4;32;40mTenho 19 anos\33[m')

n1 = 2
n2 = 4
print('\nOs valores são \033[31m{}\033[m e \033[34m{}'.format(n1, n2))