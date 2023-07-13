## Crie um algoritmo que leia o preço de um produto e retorne seu novo preço aplicando 5% de desconto.
valor = float(input('Digite o valor do produto:'))
desconto = valor*5/100
print('O valor do produto com desconto de 5% é R$ {:.2f}.'.format(valor-desconto))
