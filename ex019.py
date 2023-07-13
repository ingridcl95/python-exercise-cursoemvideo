#faça um algoritmo que leia o nome de quatro alunos e mostre na tela o nome de um deles (como um sorteio)
import random
nome1 = str(input('Digite o nome do aluno: '))
nome2 = str(input('Digite o nome do aluno: '))
nome3 = str(input('Digite o nome do aluno: '))
list_names = [nome1,nome2,nome3]

print('O nome escolhido foi: {}.'.format(random.choice(list_names)))
