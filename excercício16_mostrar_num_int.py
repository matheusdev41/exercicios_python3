#Crie um programa que leia um número  Real e mostre apenas o seu valor inteiro na tela
import math
num=float(input('Digite um valor:'))
print('O valor digitado foi {} e a sua porção inteira {}'.format(num,math.trunc(num)))
