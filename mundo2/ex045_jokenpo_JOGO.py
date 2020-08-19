# Crie um programa que faça o computador jogar Jokenpô com você
#empate, derrota, vitoria

from random import randint
from time import sleep
print('='*20)
print('JOKENPÔOOOO')
print('='*20)

#itens
itens = ('Pedra', 'Papel', 'Tesoura')
#biblioteca escolhe numero
pc = randint(0, 2)

print('''
[ 0 ]PEDRA
[ 1 ]PAPEL
[ 2 ]TESOURA''')

jogador = int(input('Escolha uma opção: '))
print('-='*10)
print('PC jogou:',itens[pc])# integra o randint à lista
print('O jogador jogou:',itens[jogador])
print('-='*10)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
############################
sleep(2)
print('*'*10)

if pc == 0: #pc jogou PEDRA
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('\033[7;31;47mVITÓRIA\033[m')
    elif jogador == 2:
        print('DERROTA')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 1: #pc jogou PAPEL
    if jogador == 0:
        print('DERROTA')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('\033[7;31;47mVITÓRIA\033[m')
    else:
        print('JOGADA INVÁLIDA')
elif pc == 2 : #pc jogou TESOURA
    if jogador == 0:
        print('\033[7;31;47mVITÓRIA\033[m')
    elif jogador == 1:
        print('DERROTA')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('JOGADA INVÁLIDA')
print('*'*10)