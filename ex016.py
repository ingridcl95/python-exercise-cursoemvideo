# Crie um algoritmo que leia um número real qualquer pelo teclado e mostra na tela sua porção inteira
import math

num = float(input('Digite um número: '))
print('A porção inteira de {} é {}'.format(num, math.trunc(num)))