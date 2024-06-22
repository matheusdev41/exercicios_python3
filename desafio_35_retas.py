a=float(input('Medida da linha 1 do triângulo: '))
b=float(input('Medida da linha 2 do triângulo: '))
c=float(input('Medida da linha 3 do triângulo: '))
#cada um desse seguimentos tem que ser menor que a soma dos outros 2
if a < b+c and b< a+c and c < a+b:
    print('Os seguimentos acima PODEM FORMAR um triângulo')
else:
    print('Os seguimentos acima NÃO PODEM FORMAR um triângulo')

