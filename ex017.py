#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa
import math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))
print('-'*12)
print('O valor da hipotenusa dos catetos {} e {} é {:.2f}'.format(co, ca, math.hypot(co, ca)))