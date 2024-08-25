
print('Vamos descobrir qual o maior valor')
um = int(input('\033[31mDigite o primeiro número\033[m: '))
dois = int(input('\033[36mDigite o segundo número\033[m: '))
print('-=-' * 20)
if um > dois:
    print(f'{um} é maior que {dois}')
elif dois == um:
    print(f'{um} é igual a {dois}')
else:
    print(f'{dois} é maior que {um}')