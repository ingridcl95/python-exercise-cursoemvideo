#Crie um programa que leia o nome de uma pessoa e diga se ela tem SILVA no nome
nome = str(input('Digite seu nome completo: ').strip())
print('-'*12)
print('SILVA' in nome.upper())