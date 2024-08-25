
def sexo():
    return str(input('\033[1;3;34m'
                     'digite qual o seu sexo\nM(masculino) F(feminino):')).strip().upper()[0]





while sexo() not in 'MF':
    print('\033[1;3;31mtente novamente\n')
print('\n\033[1;3;4;36mseu cadastrado foi finalizado.')