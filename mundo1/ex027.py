# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input("nome completo: ")).strip()
n = nome.split()
print('o primeiro nome: {}'.format(n[0]))
print('o último nome: {}'.format(n[-1]))