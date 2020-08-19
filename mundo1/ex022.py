#ler o nome e mostrar o nome com letras maisculas, minusculas, quantas letras sem
# espaço e quantas letras tem o primeiro nome

#não esquecer do str
nome = str(input('digite seu nome para análise: ')).strip()  #corta o espaços inuteis
print('seu nome : ')
print(nome.upper())
print(nome.lower())
print('Ao todo seu nome tem: {}'.format(len(nome) - nome.count(' ')))#retira o esapço no meio do nome
print('o primeiro nome tem {} letras'.format(nome.find(' ')))#encontra o nome antes do espaço da posição inicial
