# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Escreva uma frase: ')).upper().strip() #joga para maiusculo e faz a contagem

print('Ao todo, a letra "A" aparece: {} vezes'.format(frase.count('A')))
print('A primeira letra "A" aparece na posição {}'.format(frase.find('A')+1))
print('A ultima letra "A" aparece na posição {}'.format(frase.rfind('A')+1))
