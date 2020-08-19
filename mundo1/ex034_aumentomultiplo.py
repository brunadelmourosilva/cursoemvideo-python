#ler o valor do salario
#se for maior que 1.250 calcule um aumento de 10%
#se for igual ou inferior calcule um aumento de 15%

sal = float(input('digite o valor do salário para calcular seu aumento: '))

if sal > 1250:
    a = sal * 1.10
    print('o novo salário é de R${:.2f}'.format(a))
if sal <= 1250:
    b = sal * 1.15
    print('o novo salário é de R${:.2f}'.format(b))


