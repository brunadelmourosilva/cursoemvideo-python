#mostrar a parte inteira de um número real

from math import trunc
num = float(input('numero: '))

print('a parte inteira de {} é {}'.format(num, trunc(num)))