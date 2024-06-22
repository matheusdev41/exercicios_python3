cid=str(input('Em que cidade você nasceu?: ')).strip()
print(cid[:5].upper() == 'SANTO')
#cid[5] pega da primeira letra e vai até a 5 (EXCLUINDO A 5)  SANTO
#                                                             01234
#.upper() colocar tudo em maiúsculo
#== VERIFICANDO SE (cid[5].upper é igual a 'SANTO' (digitado de qualquer maneira)