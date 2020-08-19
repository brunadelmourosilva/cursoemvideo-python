#Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
#No final, mostre qual foi o maior e o menor peso lidos.

print('\033[1;31;40m---Verificador de pesos---\033[m')
list = []
for i in range(1, 6):
    p = float(input('{} - Qual o seu peso? '.format(i)))
    list.append(p) #insere valores na lista

print('\nMaior peso: {}Kg'.format(max(list)))
print('Menor peso: {}Kg'.format(min(list)))