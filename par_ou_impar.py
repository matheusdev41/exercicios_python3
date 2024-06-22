numero = int(input('Escreva um número: '))
print('Analizando...')
resultado = numero % 2
if resultado == numero:
    print('O número {} é impar'.format(numero))
else:
    print('O número {} é par'.format(numero))
