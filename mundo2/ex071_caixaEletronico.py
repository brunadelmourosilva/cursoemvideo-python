#Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico.
#No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa
#vai informar quantas cédulas de cada valor serão entregues. OBS:
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('='*20)
print('\tBANCO CBIF')
print('='*20)

cinquenta = 50
vinte = 20
dez = 10
um = 1
div = rest = 0
while True:
    val = int(input('Que valor você deseja sacar? R$'))

    div = val // cinquenta
    if div > 0: print(f'Total de {div} cédula(s) de R$50')
    rest = val % cinquenta

    div = rest // vinte
    if div > 0: print(f'Total de {div} cédula(s) de R$20')
    rest = rest % vinte

    div = rest // dez
    if div > 0: print(f'Total de {div} cédula(s) de R$10')
    rest = rest % dez

    div = rest // um
    if div > 0: print(f'Total de {div} cédula(s) de R$1')
    rest = rest % um

    op = ' '
    while op not in 'SN':
        op = str(input('\nDeseja continuar? [S/N] ')).upper().strip()[0]

    if op == 'N': break

print('='*20)
print('Volte sempre ao banco CBIF! Tenha um bom dia...')





