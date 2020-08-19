#fazer o computador pensar em um numero de 0 a 5 para o usuario tentar descobrir qual foi
#o numero escolhido pelo pc. O programa deverá escrever se o usuário venceu ou não

from random import randint
from time import sleep

pc = randint(0, 5)#faz o pc 'PENSAR'
print('-'*20)
print('Tente adivinhar hehe')
print('-'*20)
joga = int(input("Escolha um número entre 0 e 5: "))#tenta
print('PROCESSANDO...')
sleep(3)

if pc == joga:
    print('Você venceu meu chapa!')
else:
    print('Eu venci, bjs!Meu número foi o {} e o seu foi o {}'.format(pc,joga))






