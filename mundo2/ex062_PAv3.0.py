# Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais
# alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos.


from time import sleep
print('\t--- Exibindo os 10 primeiros termos de uma progressão aritmética ---\n')
a1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a razão da PA: '))
sleep(2)

termo = a1
cont = 1
t = 0
maisTermos = 10
while maisTermos != 0:
    t += maisTermos
    while cont <= t:
        print('{}'.format(termo), end=' -> ')
        termo += r
        cont +=1
    print('STOP')
    maisTermos = int(input('\nQuantos termos você quer mostrar a mais? '))

sleep(1)
print('Progressão finalizada com um total de {} termos.'.format(t))
print('Programa encerrado...')

