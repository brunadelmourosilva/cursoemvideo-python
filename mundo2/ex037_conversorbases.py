# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
#escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('digite um número: '))

print('Escolha o tipo de conversão: ')
print('[1]BINÁRIO')
print('[2]OCTAL')
print('[3]HEXADECIMAL')

opção = int(input('sua opção: '))

if opção == 1:
    print('O número {} convertido para BINÁRIO é {}'.format(num,bin(num)[2:]))
elif opção == 2:
    print('O número {} convertido para OCTAL é {}'.format(num,oct(num)[2:]))
elif opção == 3:
    print('O número {} convertido para HEXADECIMAL é {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida, tente novamente!')