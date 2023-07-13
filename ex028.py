#crie um programa que faça o computaoor pensar em um número entre 0 e 5 e peça pra o usuário tentar desoobrir
#após digitar o número, deverá mostrar se o usuário acertou ou errou

import random
from time import sleep
#faz o pc 'dormir' por um tempor determinado

print("-=-"*20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-"*20)
n1 = int(input("Em que número eu pensei? "))
sleep(3)
pc = random.randint(0,5)
if n1 == pc:
    print('Parabéns, você acertou!')
else:
    print('Poxa, você errou! Eu pensei no número {}!'.format(pc))
