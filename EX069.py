
mu = hm = tot = 0
while True:
    print('=' * 20)
    print('CADASTRE UMA PESSOA')
    print('=' * 20)
    idd = int(input('Idade:'))
    sex = qr = ' '
    while sex not in 'MF':
        sex = str(input('Sexo:')).upper().strip()[0]
    print('=' * 20)
    while qr not in 'SN':
        qr = str(input('Quer continuar?')).upper().strip()[0]
    if idd > 18:
        tot += 1
    if sex == 'M':
        hm += 1
    if sex == 'F' and idd < 20:
        mu += 1
    if qr == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {tot}')
print(f'Ao todo temos {hm} homem(s) cadastrados.')
print(f'Temos {mu} mulher(s) com menos de 20 anos.')