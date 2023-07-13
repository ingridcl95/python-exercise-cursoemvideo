"""Melhore o desafio 28 onde o computador pensa em um número entre 0 e 10. Só que agora
o jogador vai tentar adivinhar até acertar. No final, mostre quantos palpites até o acerto."""
import random
from random import randint
from time import sleep

print("\033[33m=*\033[m"*18)
print("Vou pensar em um número entre 0 e 10. \nTente adivinhar!")
print("\033[33m=*\033[m"*18)
n1 = int(input("Em qual número eu pensei?"))
pc = randint(0, 10)
palpite = 0

while n1 != pc:
    print("Você errou! Tente de novo!")
    n1 = int(input("Em qual número eu pensei?"))
    palpite += 1
print("\n\033[35mAcertou!\033[m Eu pensei no número {}. \nVocê deu {} palpites.".format(pc, palpite))
