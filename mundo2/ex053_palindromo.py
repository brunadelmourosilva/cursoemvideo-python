#Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
#desconsiderando os espaços.

frase = str(input('insira a frase: ')).lower().strip()
spl = frase.split() #vetor
unir = ''.join(spl)
inv = ''
for i in range(len(unir)-1, -1, -1):
    inv += unir[i]

if inv == unir:
    print('A frase é um palímdromo!')
else:
    print('A frase não é um palíndromo...')
    print('Frase original sem espaços: ', unir)
    print('Frase invertida: ', inv)