"""Escreva um programa que leia o ano de nascimento de um atleta e mostre sua categoria de acordo com a idade:
até 9 mirim, até 14 infantil, até 19 junior, até 25 senior, maior que 25 master"""
from datetime import date
from time import sleep

print("-="*12)
print("DESCUBRA SUA CATEGORIA")
print("-="*12)
yearborn = int(input("INFORME SEU ANO DE NASCIMENTO: "))
print("ANALISANDO, AGUARDE...")
sleep(3)
current_year = date.today().year
age = current_year-yearborn

if age <= 9:
    print("IDADE: {}. SUA CATEGORIA É: MIRIM".format(age))
elif age <= 14:
    print("IDADE: {}. SUA CATEGORIA É: INFANTIL".format(age))
elif age <= 19:
    print("IDADE: {}. SUA CATEGORIA É: JUNIOR".format(age))
elif age <= 25:
    print("IDADE: {}. SUA CATEGORIA É: SENIOR".format(age))
else:
    print("IDADE: {}. SUA CATEGORIA É: MASTER".format(age))
