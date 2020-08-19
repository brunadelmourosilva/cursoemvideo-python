#Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e
# mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.


print('-' * 20)
print('Sequência de Fibonacci')
print('-' * 20)

n = int(input('Quantos termos você gostaria de visualizar? '))

# 0    1    1    2    3    5...
# f1   f2   f3(tab)
fib1 = 0
fib2 = 1
print('{} - {}'.format(fib1, fib2), end='')
cont = 3
while cont <= n:
    fib3 = fib1 + fib2
    print(' - {}'.format(fib3), end='')

    #transição de variáveis
    fib1 = fib2
    fib2 = fib3

    cont += 1
print(' - FIM...')