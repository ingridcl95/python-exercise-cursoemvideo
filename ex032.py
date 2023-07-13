#ler um ano e informar se ele é bissexto ou não
from time import sleep
from datetime import date
print('--- DESCUBRA SE O ANO É BISSEXTO ---')
ano = int(input('Digite o ano que quer analisar ou 0 para analisar o ano atual: '))
print('-- Analisando o ano... --')
sleep(3)

if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} não é Bissexto".format(ano))
else:
    print("O ano {} é Bissexto".format(ano))



