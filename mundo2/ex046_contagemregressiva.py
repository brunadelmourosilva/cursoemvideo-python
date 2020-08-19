#contagem regressiva de fogos de artificio com 1 segundo de pausa


print('=-=-=-=CONTAGEM DE FOGOS DE ARTIFÍCIO=-=-=-=')

from time import sleep

n = int(input('Sua contagem começa em qual número? '))

for cont in range(n,-1,-1):
    sleep(1)
    print(cont)
print('ANO NOVO')