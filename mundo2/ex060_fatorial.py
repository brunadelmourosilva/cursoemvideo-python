#fatorial com while

n = int(input('Digite um número para visualizar seu fatorial: '))

num = n
fat = 1

print('{}! : '.format(n), end='')
while num > 0:
    print('{}'.format(num), end=' ')
    print(' x ' if num > 1 else ' = ', end='')
    fat *= num
    num -= 1

print(' {}'.format(fat))

#for c in range(n, 1, -1):
#   fat *= c

