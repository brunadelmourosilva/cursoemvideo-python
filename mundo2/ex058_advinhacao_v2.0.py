#Exercício Python 058: Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em
#um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
#mostrando no final quantos palpites foram necessários para vencer.


from random import randint
from time import sleep

pc = randint(0, 10) #faz o pc 'PENSAR'
print('-'*20)
print('Tente adivinhar meu número hehe')
print('-'*20)

correto = False
cont = 0

while not correto:
    jogador = int(input("\nEscolha um número entre 0 e 10: "))
    cont += 1
    print('\nPROCESSANDO...')
    sleep(2)
    if pc == jogador:
        correto = True
        print('\nVocê venceu meu chapa!')
    else:
        print('\nEu venci, bjs! Tente novamente')

print('Você acertou ultilizando {} tentativas!'.format(cont))
input('Aperte \033[7m ENTER \033[m para finalizar o jogo...')

