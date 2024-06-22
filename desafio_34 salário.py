sal=int(input('Qual o seu salário? '))
if sal > 1250:
    print('O valor do seu aumento será {:.2f}'.format(sal*0.10))
else:
    print('O valor do seu aumento será {:.2f}'.format(sal*0.15))
