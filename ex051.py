"""Leia o primeiro termo e a razão de uma progressão aritmética.
No fim, mostre os 10 primeiros termos dessa progressão"""

print("\033[33m=*\033[m"*12)
print("10 TERMOS DE UMA P.A")
print("\033[33m=*\033[m"*12)
razao = int(input("INFORME A RAZÃO: "))
primeirot = int(input("INFORME O PRIMEIRO TERMO DA PROGRESSÃO: "))
decimo = primeirot + (10-1) * razao

for c in range(primeirot, decimo + razao, razao):
    print(c, end=" → ")

