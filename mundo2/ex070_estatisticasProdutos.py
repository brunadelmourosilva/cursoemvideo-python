

print('=-'*15)
print('\tLOJA FIQUE EM CASA')
print('=-'*15)

total = qtd = cont = 0
nomeMenorProd = ''
while True:
    nomeProduto = str(input('Nome do produto: '))
    precoProd = float(input('Preço: R$'))
    print('-'*20)

    # para se caso o usuário digitar somente 1 produto
    cont += 1

    #total gasto
    total += precoProd

    #quantos produtos custam mais de R$1000.00
    if precoProd >= 1000: qtd += 1

    #nome do produto mais barato
    if cont == 1:
        menorPreco = precoProd
    else:
        if precoProd < menorPreco:
            menorPreco = precoProd
            nomeMenorProd = nomeProduto


    op = ' '
    #validação
    while op not in 'SN':
        op = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]

    if op == 'N': break

print('-'*20)
print('----- FIM -----')
print(f'O total da compra foi R${total:.2f}')
print(f'Tem-se {qtd} produto(s) custando mais de R$1000.00')

#condição para caso o caso de houver apenas um produto cadastrado
if cont == 1:
    print(f'O produto mais barato foi "{nomeProduto}" com o preco de R${menorPreco:.2f}')
else:
    print(f'O produto mais barato foi "{nomeMenorProd}" com o preco de R${menorPreco:.2f}')
