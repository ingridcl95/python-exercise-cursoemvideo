#ler 3 números e mostrar qual maior e qual o menor
from time import sleep
n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número:"))
print("--- Analisando os números... ---")
sleep(2)
'''if n1 > n2 and n1 > n3:
    print("{} é o maior número.".format(n1))
elif n2 > n1 and n2 > n3:
    print("{} é o maior número.".format(n2))
else:
    print("{} é o maior número.".format(n3))'''

#verficando quem é menor:
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
#verificando maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
print("O menor valor digitado é {}.".format(menor))
print("O maior valor digitado é {}.".format(maior))
