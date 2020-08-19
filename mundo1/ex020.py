# O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem
# sorteada.


from random import choice,shuffle
aluno1 =str(input('escreva o nome do aluno 1 : '))
aluno2 = str(input('escreva o nome do aluno 2 : '))
aluno3 = str(input('escreva o nome do aluno 3 : '))
aluno4 = str(input('escreva o nome do aluno 4 : '))
lista = [aluno1,aluno2,aluno3,aluno4]
shuffle(lista)#embaralha

print('o escolhido é ')
print(lista)