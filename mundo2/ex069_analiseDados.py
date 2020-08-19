#Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos.


cont = contIdade = contHomens = contMulheres = 0
while True:
    cont += 1
    print('-'*20)
    print('CADASTRO', cont)
    print('-'*20)

    i = int(input('Idade: '))
    # pessoas com mais de 18 anos
    if i >= 18: contIdade += 1

    s = ' ' # a cada loop, a variavel sexo passa a conter esse valor suposto para entrar na validação
    #validação
    while s not in 'MF':
        s = str(input('Sexo: [M/F]')).upper().strip()[0]
    print('-' * 20)

    #total de homens cadastrados
    if s == 'M': contHomens += 1

    #total de mulheres com menos de 20 anos
    if s == 'F' and i < 20: contMulheres += 1

    op = ' '
    #validação
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

    if op == 'N':
        break

print('\n=== FIM ===')
print(f'Total de pessoas com mais de 18 anos: {contIdade}')
print(f'Total de homens cadastrados: {contHomens}')
print(f'Total de mulheres com menos de 20 anos: {contMulheres}')