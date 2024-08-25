real = float(input('Quato voce tem na carteira? R$ '))
dolar = real / 5.11
print('Com {:.2f} voce pode comprar US$ {:.2f}'.format(real, dolar))
if dolar / 5.11:
    var = input('Voce dejesa comprar? ')
    var1 = 'sim'
    if var1 == 'sim':
        print('Voce comprou {:.2f} Dolar'.format(dolar))