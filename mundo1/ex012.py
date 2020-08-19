#desconto do produto
produto = float(input('digite o preço do produto: '))
pdesc = float(input('digite o desconto à ser dado ao produto: '))

cal =(pdesc * produto) / 100
novodesc = produto - cal
print('o desconto concedido será de R${:.2f}.'.format(cal))
print('o novo valor do produto é de R${}'.format(novodesc))
