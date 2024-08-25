

@dvieirazzy
há 1 ano (editado)
Resolvi esse exercício sem utilizar as estruturas condicionais, achei bem mais simples:

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite um último número: '))
l = [n1, n2, n3]
l.sort()
print(f'O maior número é {l[2]} e o menor é {l[0]}')