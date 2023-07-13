"""Faça um programa que mostre uma contagem regressiva para o estouro dos fogos de artíficio,
indo de 10 a 0, com pausa de um segundo entre eles."""
from time import sleep
import emoji
print("\033[1;30m=*\033[m"*10)
print("\033[1;33mCONTAGEM REGRESSIVA\033[m")
print("\033[1;30m=*\033[m"*10)

for c in range(10, -1, -1):
    sleep(1)
    print("\033[1m{}\033[m".format(c))
print(emoji.emojize("\033[1;33mFELIZ ANO NOVO! :sparkler:"))
