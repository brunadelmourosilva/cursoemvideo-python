#soma entre todos os numeros impares e que sejam multiplos de 3 entte o intervalo 1 e 500

s = 0
contador2 = 0
for cont in range(1,500+1):
    if cont % 2 !=0 and cont % 3 == 0:
        contador2 += 1 #ou contador2 +=
        s += cont      #soma de todos os elementos
#print(s, end=' ')
print('A soma dos {} números são {}'.format(contador2, s))