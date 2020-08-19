#ler o nome de uma cidade e dizer se ela começa ou não com o nome'santo'

nome = str(input('digite seu nome para análise: ')).strip()
print(nome[:5].upper() == 'SANTO')

