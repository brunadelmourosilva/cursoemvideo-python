#area de uma parede

l = float(input('qual a largura em metros: '))
a = float(input('qual a altura em metros: '))


area = l * a
qtdtinta = area / 2

print('a area da parede é {:.3f}m2 e quantidade de tinta é {:.3f}l'.format(area,qtdtinta))