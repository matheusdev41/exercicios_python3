n1=int(input('Digite um valor:'))
n2=int(input('Digite outro valor:'))
s=n1+n2
m=n1*n2
d=n1/n2
p=n1**n2
print('A soma vale {},\n o produto é {},\n a divisão é {:.3f},\n '.format(s,m,d),end='')
#print( 'A soma vale {}, o produto é {} e a divisão {:.3f}'.format(s,m,d))
                                                    #escolher casas décimais {:.número+f}
                                                                        #end= não pula a linha, mantém o cod na mesma linha
                      #\n para pular a linha
print('e a potência é {:.3f}.'.format(d,p))



