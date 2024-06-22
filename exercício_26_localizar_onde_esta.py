frase=str(input('Digite uma frase: ')).upper()
#.upper() para deixar tudo maiúsculo e o programa reconhecer o cacter digitado ( a, A,)
print('A letra a aparece {} vezes'.format(frase.count('A')))
#contando a quantidades de 'a' que aparece na frase
print('A letra a aparece a primeira vez na posição {}'.format(frase.find('a')+1))
#a posição 0 seria a primeira posição que o 'a' apareceria, por isso o +1 para pular uma casa tornando a posição 1
print('A letra a aparece por último na posição {}'.format(frase.rfind('a')))
#rfind, procurar a partir da direita

