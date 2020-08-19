#Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor
#valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


op = 'Ss'
cont = 0
med = 0
while op not in 'Nn':
    n = int(input('Digite um número: '))
    cont += 1 #quantidade de números
    med += n #média

    if cont == 1:
        menor = maior = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    op = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]

print('Você digitou {} valores e a média entre eles é igual a {:.2f}!'.format(cont, (med / cont)))
print('O maior valor lido foi o número {} enquanto menor valor foi o número {}!'.format(maior, menor))

