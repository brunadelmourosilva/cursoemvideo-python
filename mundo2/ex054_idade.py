#Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
atual = date.today().year
contJovem = 0
contAdulto = 0
for i in range(1, 7+1):
    y = int(input('Insira o ano de nascimento da pessoa {}: '.format(i)))
    idade = atual - y
    if idade >= 18:
        contAdulto += 1
    else:
        contJovem += 1

print('\033[1;35;40m {} \033[m pessoa não copletaram 18 anos.'. format(contJovem))
print('\033[1;31;44m {} \033[m pessoas já copletaram 18 anos.'. format(contAdulto))