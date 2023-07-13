"""Escreva uma programa que leia o sexo de uma pessoa e só aceite M ou F.
Caso esteja errado, peça a digitação novamente até obter o valor certo."""

sexo = str(input("Informe o sexo: ")).lower()

while sexo != 'f' and sexo != 'm':
    sexo = str(input("Opção incorreta. Favor, tente novamente.\nInforme o sexo: ")).lower()
print("Obrigado!")





