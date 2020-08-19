#quem é maior e quem é menor
from builtins import map

v1 = int(input('valor 1:' ))
v2 = int(input('valor 2:' ))
v3 = int(input('valor 3:' ))

menor = v1 #teste
#verificando o menor
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v2 and v3 < v1:
    menor = v3

maior = v1 #teste
#verificando o maior
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v2 and v3 > v1:
    maior = v3
print('o maior é ',(maior))
print('o menor é ',(menor))
