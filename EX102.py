# Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular
# e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

# Função Fatorial
def fatorial (n, show=False):
    """
    fatorial(n, show)
    => FUNÇÃO FATORIAL:
    Função que calcula o fatorial de um número.

    * PARÂMETORS
    :param n: Número que deseja-se calcular o fatorial.
    :param show: (Opcional) mostra o processo de cálculo (fatores). por Default seu valor é False.
    :return: O valor do fatorial de um número n.
    """

    fat = 1
    for i in range(n, 0, -1): # Laço para calcular o fatorial do número
        fat = fat * i

    print(f" {n}! = {fat}") # Imprime o fatorial na tela

    if show == True: # Verifica se deseja mostrar o processo dos fatores
        print(f"Cálculo:\n{n}! = ",end="")
        while n > 1:
            print(f"{n} x ", end="")
            n = n - 1

        print("1")




# PROGRAMA PRINCIPAL

help (fatorial)

# Recebe o valor do usuário
num = int(input("Digite o valor de um número inteiro: "))
while num < 0: # Verifica se o usuário digitou um número igual ou maior que zero
    print("Não há fatorial de números negativos, por favor tente novamente...")
    num = int(input("Digite o valor de um número inteiro positivo: "))

# Verifica se o usuário deseja ver os fatores da conta
pergunta = input("Deseja ver os fatores do cálculo? [S/N}: ").lower()[0]
while pergunta not in 'sn': # verifica se a opção digitada é válida
    print("Opção inválida, tente novamente...")
    pergunta = input("Deseja ver os fatores do cálculo? [S/N}: ").lower()[0]
if pergunta == 's':
    show = True
else:
    show = False
