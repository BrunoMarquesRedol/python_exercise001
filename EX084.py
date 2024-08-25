

#feito no vídeo:
for p in princ:
    if p[1] == men:
        print(f'[{p[0]}]', end=' ')


#dá pra fazer assim também:
for nome, peso in princ:
    if peso == men:
        print(nome, end=' ')


Como cada item de princ tem dois valores, o primeiro valor vai pra 'nome' e o segundo, pra 'peso'