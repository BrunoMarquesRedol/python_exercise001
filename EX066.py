

soma = cont = 0
while True:
    n = int(input("digite um valor (999 para parar) "))
    if n == 999:
        break
    soma += n
    cont += 1
print(f"você digitou {cont} números e a soma entre eles foi de {soma}.")