import random
alun1=str(input('Digite o nome do aluno 1: '))
alun2=str(input('Digite o nome do aluno 2: '))
alun3=str(input('Digite o nome do aluno 3: '))
alun4=str(input('Digite o nome do aluno 4: '))
lista=[alun1,alun2,alun3,alun4]
random.shuffle(lista)
#random.shuffle embaralha os elementos combinados nas [] = lista
print('A ordem de apresentação será\n {}'.format(lista))


