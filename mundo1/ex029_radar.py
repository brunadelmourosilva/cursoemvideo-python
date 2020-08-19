#ler a velocidade de um carro e se ultrapassar 80km/h ele foi multado
#a multa será de 7.00 por Km acima do limite
cores={'limpa':'\033[m',
        'negritoazulwhite': '\033[1;34;40m'
}


vel = float(input('Qual foi a velociade do carro? '))

if vel>80:
    print('\033[1;35m-\033[m'*20)

    print('\033[1;31;40mPerdeu meu chapa, você foi multado!\033[m')
    print('\033[1;31;40mSua multa será de: \033[m')

    print('{}R${:.2f}'.format(cores['negritoazulwhite'],(vel - 80)* 7.00),'\033[m')

    print('\033[1;35m-\033[m'*20)

else:
    print('\033[4   ;35;44mVocê está dentro do limite, boa viagem!\033[m')