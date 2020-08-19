#ler um número de 0 a 9999 e separe por casas

#formato string
#num = int(input('digite um número: '))
#n = str(num)
#print('unidade: ',n[3])
#print('dezena: ',n[2])
#print('centena: ',n[1])
#print('milhar: ',n[0])

#forma matematica
num = int(input('digite um número: '))

u = num //1 % 10
d = num //10 % 10
c = num //100 % 10
m = num //1000 % 10
print('unidade: ',u)
print('dezena: ',d)
print('centena: ',c)
print('milhar: ',m)
