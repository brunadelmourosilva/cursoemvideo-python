 # Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade
 # , se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já
 # passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta
 # ou que passou do prazo.

from datetime import date
anonasc = int(input('Informe seu ano de nascimento: '))

anoatual = date.today().year
idade = anoatual - anonasc

if idade < 18:
    falta = 18 - idade
    print('Você ainda não atingiu a idade exata para o alistamento!')
    print('Ainda falta {} ano(s) '.format(falta))
elif idade == 18:
    print('Você está no ano exato para o alistamento. Não perca tempo!')
else:
    passa = idade - 18
    print('Já se passou {} anos para alistamento militar. Corra o quanto antes!!!'.format(passa))