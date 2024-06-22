#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente e calcule a hipotenusa
import math
co=float(input( 'Cateto oposto: '))
ca=float(input('Cateto adjacente:'))
hi=math.hypot(co,ca)
print('A hipotenusa é {:.2f}'.format(hi))
                     #casas decimais limite{.:núme ro de casas}




