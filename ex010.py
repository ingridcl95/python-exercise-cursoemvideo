## crie um algoritmo que leia quanto uma pessoa tem na carteira e mostre quantos
# dólares ela pode comprar. Dólar = 3,27
carteira = float(input('Digite o valor em sua carteira: R$'))
dolar = 3.27
print('Com o valor de R$ {:.2f} você pode comprar U$ {:.2f} dólares.'.format(carteira, carteira/dolar))
