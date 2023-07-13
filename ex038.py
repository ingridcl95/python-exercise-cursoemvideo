"""Escreva um programa que leia dois numeros inteiros e compare-os, mostrando na tela uma mensagem:
qual o maior, qual o menor ou que não existe valor maior e eles são iguais"""
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print("O maior valor é {} e o menor valor é {}.".format(n1, n2))
elif n2 > n1:
    print("O maior valor é {} e o menor valor é {}".format(n2, n1))
else:
    print("Não existe maior valor, os números são iguais.")

