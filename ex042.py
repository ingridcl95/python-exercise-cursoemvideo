"""Refaça o desafio 35 de triângulos. Se ele puder fazer um triângulo, informe que tipo ele irá formar:
equilátero: todos os lados iguais, isosceles: dois lados iguais, escaleno: todos os lados diferentes"""
reta1 = float(input("Informe comprimento da primeira reta:"))
reta2 = float(input("Informe comprimento da segunda reta:"))
reta3 = float(input("Informe comprimento da terceira reta:"))

if reta1 < reta2+reta3 and reta2 < reta1+reta3 and reta3 < reta1+reta2:
    if reta1 == reta2 == reta3:
        print("Suas retas formam um triângulo equilátero.")
    elif reta1 != reta2 != reta3 != reta1:
        print("Suas retas forma um triângulo escaleno.")
    else:
        print("Suas retas formam um trinângulo isósceles.")
else:
    print("Suas retas não podem formar um triângulo.")

