##Faça um algoritmo que leia o salário de um funcionário e retorne o novo valor com aumento de 15%.
salario = float(input('Digite o valor do salário: R$ '))
aumento = salario*15/100
print('-'*17)
print('O valor do salário com aumento de 15% é R$ {:.2f}.'.format(salario+aumento))