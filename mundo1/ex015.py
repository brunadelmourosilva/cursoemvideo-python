#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e
#a quantidade de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado

km = float(input('qual a quantidade de Km percorridos: '))
dia = int(input('por quantos dias o carro foi alugado: '))

preco = (dia * 60) + (km * 0.15)

print('o preço total do alguel é de R${:.2f}'.format(preco))