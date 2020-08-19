#leia dois numeros que faça comparações entre eles

num1 = int(input('NÚMERO 1: '))
num2 = int(input('NÚMERO 2: '))

if num1 > num2:
    print('{} o primeiro valor é maior'.format(num1))
elif num2 > num1:
    print('{} o segundo valor é maior'.format(num2))
else:
    print('Não existe valor maior, os dois são iguais!')