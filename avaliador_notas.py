nome=str(input('Qual é o seu nome? '))
n1=float(input('Digite a nota 1'))
n2=float(input('Digite a nota 2'))
n3=float(input('Digite a nota 3'))
media=(n1+n2+n3)/3
print('A sua média foi {:.2f}'.format(media))
if media >= 6:
    print('Meus parabéns {}, você foi aprovado'.format(nome))
else:
    print('{}, infelizmente você foi reprovado'.format(nome))
print('Nos vemos ano que vem!')