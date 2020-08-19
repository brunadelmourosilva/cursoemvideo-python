#Exercício Python 52: Faça um programa que leia um
#número inteiro e diga se ele é ou não um número primo.

n = int(input('numero: '))
cont = 0
for i in range(1, n+1):
    if n % i == 0:
        print('\033[33m', end='')
        cont += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(i), end='')

if cont == 2:
    print('\no numero eh primo')
else:
    print('\nnao eh primo')