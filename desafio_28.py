import random
lista=[1,2,3,4,5]
correto=random.choice(lista)
escolhido=int(input('Qual número será sorteado?'))
if escolhido == correto:
    print('Você acertou, o número sorteado foi {}.'.format(correto))
else:
    print('Você errou, o número sorteado foi {}'.format(correto))
print('Seu trouxa')
