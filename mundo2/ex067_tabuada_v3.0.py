#Exercício Python 67: Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.


while True:
    cont = 0 #reinicia o contador a cada loop
    n = int(input('Quer ver a tabuada de qual valor? '))
    print('-'*30)

    if n < 0:
        break

    while cont < 10:
        cont += 1
        print(f'{n} x {cont} = {n * cont}')
    print('-'*30)

print('PROGRAMA TABUADA ENCERRADO...')