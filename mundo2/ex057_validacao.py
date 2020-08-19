
s = str(input('Digite o sexo [M/F]: ')).upper().strip()
while s not in 'MmFf':
    print('Caracter incorreto. Digite novamente!', end='')
    s = str(input('[M/F]: ')).upper().strip()

print('Fim...')