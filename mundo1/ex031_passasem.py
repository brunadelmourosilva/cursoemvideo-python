#leia a viagem em Km e em seguida, calcule o preço cobrando 0,50 por Km por viagens ate 200Km
#e 0,45 para viagens mais longas

km = float(input('Qual a distância percorrida em km? '))

p1 = km * 0.50
p2 = km * 0.45

if km < 200:
    print('O preço da viagem de {:.0f} Km ficará em R${:.2f}!'.format(km, p1))

else:
    print('O preço da viagem de {:.0f} Km ficará em R${:.2f}!'.format(km, p2))