# Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - EQUILÁTERO: todos os lados iguais
# - ISÓSCELES: dois lados iguais, um diferente
# - ESCALENO: todos os lados diferentes

print('-='*15)
print('Analisador de Triângulos')
print('-='*15)
s1 = float(input('segmento 1: '))
s2 = float(input('segmento 2: '))
s3 = float(input('segmento 3: '))

#analisando segmento 1
r1 = s2 - s3
r11 = s2 + s3
#analisando segmento 2
r2 = s1 - s3
r22 = s1 + s3
#analisando segmento 3
r3 = s1 - s2
r33 = s1 + s2

if r1 < s1 < r11 and r2 < s2 < r22 and r3 < s3 < r33:
    #CONDIÇÃO ANINHADA
    print('É possível formar um triângulo',end='')
    if s1 == s2 == s3:
        print(' EQUILÁTERO')
    elif s1 != s2 != s3 != s1:
        print(' ESCALENO')
    else:
        print(' ISÓCELES')

else:
    print('Não é possível formar um triângulo!')





