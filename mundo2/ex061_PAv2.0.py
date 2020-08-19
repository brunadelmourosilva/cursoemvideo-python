# Progressão aritmética com while

from time import sleep

print('\t--- Exibindo os 10 primeiros termos da progressão aritmética---\n')
sleep(3)

a1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))

termo = a1
cont = 1
while cont <= 10:
    print('{}'.format(termo), end=' -> ')
    termo += r
    cont +=1 #enquanto não chegar ao número 10
print('FIM...')