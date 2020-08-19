# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

preco = float(input('Valor do produto: R$'))
print('[ 1 ] à vista dinheiro/cheque: 10% de desconto')
print('[ 2 ] à vista no cartão: 5% de desconto')
print('[ 3 ] em até 2x no cartão: preço formal')
print('[ 4 ] 3x ou mais no cartão: 20% de juros')
condicao  = int(input('Escolha: '))

#conta
avdc = preco - ((10 * preco) /100)
avc = preco - ((5 * preco) /100)
duascartao = preco / 2
trescartao = preco + ((20 * preco) / 100)


if condicao == 1:
    print(avdc)
elif condicao ==2:
    print(avc)
elif condicao == 4:
    parcela = int(input('Em quantas parcelas: '))
    parcelas = trescartao / parcela
    print('sua compra de {} ficará em {}'.format(preco, trescartao))
    print('parcelas em: {}X de {}'.format(parcela, parcelas))
elif condicao == 3:
    print('parcelas em: 2X de {}'.format(duascartao))
else:
    print('OPÇÃO INVÁLIDA')
