"""Escreva um programa que faça o computador jogar Jokenpô com vc. """
import random
from time import sleep
print("-="*10)
print("VAMOS JOGAR!")
print("-="*10)
user = int(input("""O QUE VOCÊ ESCOLHE? 
0 - PEDRA
1 - PAPEL
2 - TESOURA
DIGITE SUA ESCOLHA: """))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO")
print("-="*10)
itens = ("PEDRA", "PAPEL", "TESOURA")
pc = random.randint(0, 2)
if pc == user:
    print("EMPATAMOS!")
elif pc == 0 and user == 1:
    print("COMPUTADOR JOGOU {}.\nPAPEL EMBRULHA PEDRA!\nVOCÊ GANHOU!".format(itens[pc]))
elif pc == 1 and user == 0:
    print("COMPUTADOR JOGOU {}.\nPAPEL EMBRULHA PEDRA!\nVOCÊ PERDEU!".format(itens[pc]))
elif pc == 0 and user == 2:
    print("COMPUTADOR JOGOU {}.\nPEDRA QUEBRA TESOURA!\nVOCÊ PERDEU!".format(itens[pc]))
elif pc == 2 and user == 0:
    print("COMPUTADOR JOGOU {}.\nPEDRA QUEBRA TESOURA!\nVOCÊ GANHOU!".format(itens[pc]))
elif pc == 2 and user == 1:
    print("COMPUTADOR JOGOU {}.\nTESOURA CORTA PAPEL!\nVOCÊ PERDEU!".format(itens[pc]))
elif pc == 1 and user == 2:
    print("COMPUTADOR JOGOU {}.\nTESOURA CORTA PAPEL!\nVOCÊ GANHOU!".format(itens[pc]))
else:
    print("OPPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
