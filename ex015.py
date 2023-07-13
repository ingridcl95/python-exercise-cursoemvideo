#faça um algoritmo que leia a quantidade de dias que um carro ficou alugado, quanto km foram foram rodados.
# Calcule o total a pagar sabendo que a diária é de 60 e 0,15 por km


dias = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos km foram rodados?'))
print('-'*12)
print('O valor total a ser pago é de R$ {}'.format((dias*60)+(km*0.15)))
