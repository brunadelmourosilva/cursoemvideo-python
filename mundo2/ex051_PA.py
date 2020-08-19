# Exercício Python 051: Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
# No final, mostre os 10 primeiros termos dessa progressão


a1 = int(input('Insira o primeiro termo da PA: '))
r = int(input('Insira a Razão da PA: '))

#fórmula para encontrar o 10º termo da PA
décimo = a1 + (10-1) * r

for cont in range(a1,décimo + r ,r):
    print("{}".format(cont),end=' -> ')
print('ACABOU')