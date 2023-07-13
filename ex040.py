"""Escreva um programa que leia duas notas e calcule sua média mostrando as informações de acordo com a media:
abaixo de 5.0 está reprovado, entre 5.0 e 6.9 está de recuperação, média igual ou maior que 7.0 está aprovado"""

note1 = float(input("Digite a primeira nota: "))
note2 = float(input("Digite a segunda nota: "))
media = (note1+note2)/2

if media < 5.0:
    print("Sua média foi {:.1f}.\n Você está reprovado.".format(media))
elif 7 > media >= 5:
    print("Sua média foi {:.1f}.\n Você está em recuperação.".format(media))
elif media >= 7.0:
    print("Sua média foi {:.1f}.\n Você está aprovado!".format(media))
