#ler qualquer valor no teclado e mostre seu tipo primitivo e todas as informações possiveis

think = input('digite algo para ser analisado: ')
print(type( think))
print('espaco: ',think.isspace())
print('numerico: ',think.isnumeric())
print('maiusculo: ',think.isupper())
print('minusculo: ',think.islower())