#faça um algoritmo que leia o  nome de 4 pessoas e retorne na tela o nome delas de forma ordenada
import random
nome1 = str(input('Digite o nome do  primeiro aluno: '))
nome2 = str(input('Digite o nome do segundo aluno: '))
nome3 = str(input('Digite o nome do terceiro aluno: '))
nome4 = str(input('Digite o nome do quarto aluno: '))

list_names = [nome1,nome2,nome3,nome4]
random.shuffle(list_names)
print(list_names)