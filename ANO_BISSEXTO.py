import datetime
ano=int(input('Que ano quer analizar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano=datetime.date.today().year
    #da biblioteca datetime, vai pegar a data de hoje e pegar apenas o ano
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    # or = não pode ser divisivel por 100 OU divisivel por 400
    #!=0 isso quer dizer que ele é diferente de 0, ou seja 1,2,3...
    #ano % 4 == 0 por que ocorre de 4 em 4 anos, então o resto da sua divisão (&) tem que ser igual a 0.
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO É BISSEXTO'.format(ano))
