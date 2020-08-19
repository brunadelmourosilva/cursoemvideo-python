# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome
# do escolhido.
#str-string
from random import choice
aluno1 =str(input('escreva o nome do aluno 1 : '))
aluno2 = str(input('escreva o nome do aluno 2 : '))
aluno3 = str(input('escreva o nome do aluno 3 : '))
aluno4 = str(input('escreva o nome do aluno 4 : '))

lista = [aluno1,aluno2,aluno3,aluno4]
escolhido = choice(lista)#escolhe
print('o escolhido é {}'.format(escolhido))