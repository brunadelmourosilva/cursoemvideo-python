#Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo,
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

names = []
ages = []
med = 0
old = 0
nameOld = ''
contWom = 0
for i in range(0, 4):
    n = str(input('\nNome da pessoa {}: '.format(i+1)))
    names.append(n)

    age = int(input('Idade da pessoa {}: '.format(i+1)))
    ages.append(age)

    gender = str(input('Sexo da pessoa {} (M ou F): '.format(i+1))).strip().upper()
    #média
    med += age / 4
    #Homem mais velho
    if gender == 'M':
        if old < age:
            old = age
            nameOld = n
    #Mulheres com menos de 20 anos
    if gender == 'F' and age < 20:
        contWom += 1

print('\033[1;35m\n---------------------------------------------------------------\n\033[m')
print('Média de idade do grupo: \033[7m {} \033[m'.format(med))
print('O homem mais velho se chama \033[7m {} \033[m e ele têm \033[7m {} \033[m anos.'.format(nameOld, old))
print('Existem \033[7m {} \033[m mulher(es) com menos de 20 anos.'.format(contWom))