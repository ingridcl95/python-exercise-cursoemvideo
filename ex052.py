"""Ler um número inteiro e diga se ele é ou não um número primo"""

print("\033[33m=*\033[m"*13)
print("DESCOBRINDO NÚMEROS PRIMOS")
print("\033[33m=*\033[m"*13)
numero = int(input("Digite um número: "))

cont = 0
for c in range(1, numero+1):
    if numero % c == 0:
        cont += 1
        print("\033[34m{}\033[m".format(c), end=" ")
    else:
        print("\033[31m{}\033[m".format(c), end=" ")
print("\nO número {} foi divisível {} vezes.".format(numero, cont))
if cont == 2:
    print("Por isso ele É PRIMO.")
else:
    print("Por isso ele NÃO É PRIMO.")
