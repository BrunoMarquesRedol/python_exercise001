
no=int(input('\n Informe o Ano: '))

if ano%100==0:
    if  ano%400==0:
        print('Ano Bissexto!')
    else:
        print('Não é Bissexto!')
else:
    if ano%4==0:
        print('Ano Bissexto!')
    else:
        print('Não é Bissexto!')