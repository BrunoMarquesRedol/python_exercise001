
np = int(input('Digite um numero para verificarmos: '))
contprimo = 0

for c in range (2,np+1):
    if np%c == 0:
        print(f'O numero {np} é divisível por {c}.')
        contprimo += 1
    else:
        np%c == 1
        print(f'O numero {np} não é divisível por {c}.')

if contprimo >= 2:
    print (f'O numero {np} não é um numero primo.')
else:
    print (f'O numero {np} é um numero primo.')