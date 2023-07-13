"""Ler seis números inteiros e mostre a soma apenas dos números que forem pares."""
import emoji

print("=*"*11)
print("\033[36mSOMA DE NÚMEROS PARES\033[m")
print("=*"*11)

soma = 0
cont = 0
for c in range(1, 7):
    n = int(input("Informe o {} número: ".format(c)))
    if n % 2 == 0:
        soma = soma + n
        cont += 1
print("=*"*12)
print("Você informou {} números pares e a soma entre eles é \033[1;36m{}.\033[m".format(cont, soma))
