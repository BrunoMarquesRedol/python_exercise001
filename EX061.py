


print('\033[4;35mVejamos a progressão aritmética\033[m')
ini = int(input('Escolha o inicio: '))
razão = int(input('Escolha a razão: '))
resu = 0

while resu < 10:
    print(ini, end=', ')
    ini += razão
    resu += 1
