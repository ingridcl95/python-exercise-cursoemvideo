#crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas
#O nome com todas as letras minusculas
#Quantas letras ao todo (sem contar os espaços)
#Quantas letras tem o primeiro nome

nome = str(input('Digite seu nome completo:')).strip()
print('-'*12)
print(nome.upper())
print('-'*12)
print(nome.lower())
print('-'*12)
print(len(nome) - nome.count(' '))
#é possível fazer cálculos entre as strings
print('-'*12)
#dividido = nome.split()
print(nome.find(' '))
#ele vai procurar o primeiro espaço após o primeiro nome, retornará a qtd de letras