#Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).


num = soma = qtd = 0
num = int(input('Digite um número inteiro [tecle 999 para encerrar]: '))
while num != 999:
    soma += num
    qtd += 1
    num = int(input('Digite um número inteiro [tecle 999 para encerrar]: ')) #flag

print('Você digitou {} números e a soma entre eles foi igual a {}'.format(qtd, soma))
