# Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
# só que agora utilizando um laço for.

n = int(input('digite um número para ver sua tabuada: '))
for cont in range(1,10+1):
    print('{} X {} = {}'.format(cont, n, cont * n))