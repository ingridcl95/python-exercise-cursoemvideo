"""Ler o peso de 5 pessoas e no final mostre qual foi o maior e o menor pesos lidos"""

maior = 0
menor = 0
for pessoa in range(1, 6):
    peso = float(input("Qual o peso da {}ª pessoa?".format(pessoa)))
    if pessoa == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
            if peso < menor:
                menor = peso
print("O maior peso lido foi {:.1f}kg.".format(maior))
print("O menor peso lido foi {:.1f}kg.".format(menor))

