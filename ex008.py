## escreva um algoritmo que leia um valor em Metros e exiba o número convertido em Centímetros e Milímetros.
metro = float(input('Digite o valor em metros: '))
cm = metro*100
mm = metro*1000
print('O valor convertido em centímetros é de {:.0f}e o valor em milímetros é de {:.0f}mm.'.format(cm, mm))

