#Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
#consecutivas que ele conquistou no final do jogo.


from random import randint

print(f'=-'*12)
print('\tPAR OU ÍMPAR!')
print('=-'*12)

cont = 0
while True:
    # a variável pc irá armazenar um valor aleatório a cada loop
    pc = randint(0, 10)

    val = int(input('Escolha um número: '))
    pi = str(input('Par ou ímpar [P/I]: ')).upper().strip()[0]

    #validação de caracter
    while pi not in 'PpIi':
        print('Caracter inválido. Escolha[P/I]...')
        pi = str(input('Par ou ímpar [P/I]: ')).upper().strip()[0]

    print('-'*20)
    result = val + pc
    print(f'Você escolheu {val} e o computador {pc}. Total de {result}', end='')

    if pi == 'P' and result % 2 == 0 or pi == 'I' and result % 2 != 0:
        if result % 2 == 0:
            print('... \033[1;31;40m Deu PAR \033[m')
        else:
            print('... \033[1;33;47m Deu ÍMPAR \033[m')

        print('-'*20)
        print('\033[7m Você VENCEU!\033[m')
        print('Vamos jogar novamente...')
        print('=-'*12)
        cont += 1

    else:
        print('\n')
        print('\033[1;34;41m Você PERDEU! \033[m')
        print('=-' * 20)
        break

if cont == 1: print('\033[1;30;42m GAME OVER!\033[m Você venceu 1 vez.')
elif cont == 0: print('\033[1;30;42m GAME OVER!\033[m Você não venceu nenhuma partida.')
else: print(f'\033[1;30;42m GAME OVER!\033[m Você venceu {cont} vezes.')