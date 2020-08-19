#Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar[ 2 ] multiplicar[ 3 ] maior[ 4 ] novos números[ 5 ] sair do programa


print('\t\033[7m---MENU DE OPERAÇÕES---\033[m')
print('\t[ 1 ] SOMA')
print('\t[ 2 ] MULTIPLICAÇÃO')
print('\t[ 3 ] MAIOR')
print('\t[ 4 ] NOVOS NÚMEROS')
print('\t[ 5 ] SAIR DO PROGRAMA\n')

v1 = int(input('\nDigite o valor 1: '))
v2 = int(input('Digite o valor 2: '))
op = 0
while op != 5:
    op = int(input('Digite a operação desejada: '))

    if op == 1:
        print('A soma entre {} + {} é {}'.format(v1, v2, v1 + v2))
    elif op == 2:
        print('A multiplicação entre {} * {} é {}'.format(v1, v2, v1 * v2))
    elif op == 3:
        if v1 > v2: print('O maior número é', v1)
        else: print('O maior número é', v2)
    elif op == 4:
        v1 = int(input('\nDigite o valor 1: '))
        v2 = int(input('Digite o valor 2: '))
    elif op == 5:
        input('Aperte \033[7m ENTER \033[m para finalizar...')
    else:
        print('Opção Inválida. Tente novamente.')

    print('-=-'*10)

print('FIM...')