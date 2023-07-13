"""Faça um programa que calcule a soma de todos os números ímpares que são mútiplos de 3
e que estão no intervalo entre 1 e 500"""
print("\033[1;35;40mÍMPARES MÚLTIPLOS DE 3\033[m")
print("~"*23)

"""for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        soma = c
        print(c, end=", ")"""

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont += 1
        soma += c
print("A soma dos {} valores é igual a {}.".format(cont, soma))

