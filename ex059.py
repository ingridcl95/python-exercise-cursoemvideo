"""Crie um programa que leia dois valores e mostre um menu na tela.
1 - somar
2 - multiplicar
3 - maior valor
4 - novos números
5 - sair do programa"""
print("\033[34m=*\033[m"*12)
print("OPERAÇÕES COM 2 VALORES")
print("\033[34m=*\033[m"*12)
n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
menu = 0
while menu != 5:
    print("\nO que você quer fazer com esse valores?")
    menu = int(input(
        '\n\033[33m[1]\033[m - Somar \n\033[33m[2]\033[m - Multiplicar '
        '\n\033[33m[3]\033[m - Mostrar maior valor \n'
        '\033[33m[4]\033[m - Inserir novos números \n\033[33m[5]\033[m - Sair do programa\nDigite sua opção: '))
    if menu == 1:
        soma = n1 + n2
        print("\033[34m-\033[m" * 20)
        print("A soma de {} e {} é igual a {}.".format(n1, n2, soma))
        print("\033[34m-\033[m" * 20)
    if menu == 2:
        mult = n1*n2
        print("\033[34m-\033[m" * 20)
        print("O produto entre {} e {} é {}.".format(n1, n2, mult))
        print("\033[34m-\033[m" * 20)
    if menu == 3:
        if n1 > n2:
            print("\033[34m-\033[m" * 20)
            print("{} é o maior valor.".format(n1))
            print("\033[34m-\033[m" * 20)
        else:
            print("\033[34m-\033[m" * 20)
            print("{} é o maior valor.".format(n2))
            print("\033[34m-\033[m" * 20)
    if menu == 4:
        print("\033[34m-\033[m" * 20)
        n1 = int(input("Digite o primeiro valor: "))
        n2 = int(input("Digite o segundo valor: "))
print("\nObrigada por participar!")
