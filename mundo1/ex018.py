#ler um ângulo qualquer e mostrar o valor de seu seno, cosseno, tangente

from math import sin, cos, tan, radians

an = float(input('qual o ângulo: '))
seno = sin(radians(an))
print('o seno de {}° é {:.2f}'.format(an,seno))

cosseno = cos(radians(an))
print('o cosseno de {}° é {:.2f}'.format(an,cosseno))

tangente = tan(radians(an))
print('a tangente de {}° é {:.2f}'.format(an,tangente))
