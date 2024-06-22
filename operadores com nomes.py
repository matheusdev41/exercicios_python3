nome=input('Qual o seu nome?')
#{:>20} - nome alinhado a esquerda
print('Prazer em conhecer você,{:>20}!'.format(nome))
#{:^20} - nome centralizado
print('Prazer em conhecer você {:^20}!'.format(nome))
#{:= ou qualquer outro símbolo ^20} - centraliza o nome e preenche com a variável antes do circunflexo
print('Prazer em conhecer você {:=^20}!'.format(nome))



