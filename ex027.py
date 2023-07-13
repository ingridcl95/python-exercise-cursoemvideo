#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O primeiro e o ultimo nome separadamente.
nome = str(input('Digite seu nome completo: ')).strip()
print('-'*20)
nome = nome.split()
print('O seu primeiro nome é {}'.format(nome[0]))
print('O nome último nome é {}.'.format(nome[-1]))
