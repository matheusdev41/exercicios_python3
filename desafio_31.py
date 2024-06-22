dist=float(input('Qual a distância da viagem em km? '))
p1=0.5*dist
p2=0.45*dist
if dist >= 200:
    print('O valor da passagem será R${:.2f}'.format(p1))
else:
    print('O valor da passagem será R${:.2f}'.format(p2))



