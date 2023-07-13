"""Escreva um programa que aprove um financiamento de casa. O programa vai perguntar o valor da casa, o salário
do comprador e o prazo que ele quer pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou o empréstimo será negado"""

from time import sleep
print("-="*15)
print("SIMULADOR DE FINANCIAMENTO")
print("-="*15)
vcasa = float(input("Informe o valor da casa: R$ "))
salario = float(input("Informe o valor do salário: R$ "))
prazo = int(input("Informe o prazo em que deseja pagar: "))
print("ANALISANDO SEUS DADOS, AGUARDE...")
sleep(2)

parcela = vcasa/prazo*12
limite = salario*(30/100)
if parcela <= limite:
    print("O seu financiamento foi aprovado!")
else:
    print("Infelizmente, seu financiamento foi negado. A parcela não pode exceder 30% do seu salário.")
