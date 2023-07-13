"""Faça um programa que leia o ano de nascimento de um usuário e mostre:
se ele ainda vai se alistar, ou se está na hora de se alistar, ou se já passou do tempo para alistamento.
Deve mostrar também o tempo que falta para se alistar ou quanto tempo passou do prazo."""

from time import sleep
from datetime import date
print("-="*23)
print("CONSULTE SEU PRAZO PARA ALISTAMENTO MILITAR")
print("-="*23)
year = int(input("INFORME SEU ANO DE NASCIMENTO: "))
print("CONSULTANDO, AGUARDE...")
sleep(3)
current_year = date.today().year
age = current_year-year

print("Quem nasceu em {} tem {} anos em {}.".format(year, age, current_year))
if age < 18:
    time = 18-age
    print("Faltam {} anos para o seu alistamento.".format(time))
    print("Seu alistamento será em {}".format(current_year+time))
elif age == 18:
    print("Está na hora de se alistar! Procure o Quartel Militar mais próximo.")
elif age > 18:
    time = age-18
    print("Você perdeu o prazo! Passaram {} anos do prazo.".format(time))
    print("Você deveria ter se alistado em {}.".format(current_year-time))

