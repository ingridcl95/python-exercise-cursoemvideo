"""Ler o ano de nascimento de 7 pessoa. No final, mostre quantas pessoas
já atingiram a maior idade e quantas são menores. Maior idade = 21 anos"""
from datetime import date
maior = 0
menor = 0
atual = date.today().year
for pessoa in range(1, 8):
    anonasc = int(input("Em que ano a {}ª pessoa nasceu? ".format(pessoa)))
    idade = atual - anonasc
    if idade < 21:
        menor += 1
    else:
        maior += 1
print(maior, "pessoas atingiram a maior idade e ", menor, "pessoas ainda são menores de idade.")
