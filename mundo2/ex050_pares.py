#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.

s =0
contador=0
for cont in range(1,7):
    n = int(input('número {}: '.format(contador)))
    if n % 2 == 0:
        s = s + n
        contador+=1

print('A soma dos pares {} é {}'.format(contador,s))