
print('Digite um número e descubra sua taboada')
num = int(input('Escolha um número: '))
for c in range(1, 11):
    print(f'{num} x {c} = {num * c}')