name = str(input('Digite o seu nome: ')).strip()
if name.upper().find('SILVA') > -1:
    print('Você tem Silva no nome!')
else:
    print('Você não tem Silva no nome!')