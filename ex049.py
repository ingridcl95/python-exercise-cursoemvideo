"""Faça uma tabuada de um número escolhido pelo usuário"""

print("\033[33m=*\033[m"*20)
n = int(input("INFORME NÚMERO PARA SABER SUA TABUADA: "))
print("\033[33m=*\033[m"*20)

for c in range(0, 11):
    print("\033[1;34m{} x {} \033[m= \033[1;33m{}\033[m".format(n, c, n*c))


