#vereificar se o ano é bissexto

from datetime import date
print('coloque 0 para analisar o ano atual do PC: ')
ano = int(input('Digite um ano qualquer: '))

a = 365
ab = 366

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ANO DE {} É BISSEXTO:'.format(ano))
else:
    print('O ANO DE {} NÃO É BISSEXTO'.format(ano))