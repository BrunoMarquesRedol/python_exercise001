
print('-------Calculo de descontos abaixo-------')
Val = float(input("Escolha um valor para ser usado"))
Des = float(input("Agora escolha o desconto desejado"))

Fn = float((Val*Des)/100)
Fn2 = float(Val - Fn)

print(f'Os {Des}% de desconto equivalem a R${Fn:.2f} subtraídos do seu valor de R${Val:.2f}. Logo você pagará R${Fn2:.2f}')