#Escreva um programa para aprovar o empréstimo bancário para a compra
# de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('='*15)
print('\033[1;31;44mSIMULADOR DE EMPRÉSTIMO BANCÁRIO\033[m')
print('='*15)

val = float(input('Qual o valor da casa? '))
sal = float(input('Qual o seu salário mensal? '))
ano = int(input('Em quantos anos você pretende pagar esta parecela? '))

meses = (ano * 12);
prestacao = val / meses;
emprestimo = sal * 0.30; #valor excente estático

if prestacao < emprestimo:
    print('EMPRÉSTIMO ACEITO!')
    print('A prestação será de R${:.2f} mensais durante {} anos.'.format(prestacao,ano), end='')
    print('Haverá um desconto de R${:.2f} em seu salário de R${:.2f}'.format(emprestimo,sal))
elif prestacao > emprestimo:
    print('EMPRÉSTIMO NEGADO!')
    print('Para pagar uma casa de R${} em {} anos a prestação será de R${:.2f}'.format(val,ano,prestacao))

