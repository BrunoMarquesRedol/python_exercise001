
val = float(input('Entre com o salário do funcionário: '))
sal = val * 1.10 if val > 1250 else val * 1.15
print('Quem ganhava R${} passa a ganhar {:.2f}'.format(val, sal))