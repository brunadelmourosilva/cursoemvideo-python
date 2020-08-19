#leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

from math import pow,sqrt
cato = float(input('digite o comprimento do cateto oposto: '))
cata = float(input('digite o comprimento do cateto adjacente: '))
#teoream de pitágoras
hip = sqrt((pow(cato,2) + pow(cata,2)))

print('o valor da hipotenusa é {:.2f}'.format(hip))