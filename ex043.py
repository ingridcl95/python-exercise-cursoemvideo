"""Escreva um programa que leia o peso e a altura de uma pessoa e calcule seu IMC. Mostre seu status de acordo com a tabela abaixo:
abaixo de 18.5: abaixo do peso; entre 18.5 e 25: peso ideal; de 25 a 30: sobrepeso; 30 a 40: obesidade;
acima de 40: obesidade mórbida"""
print("-="*10)
print("CALCULE O SEU IMC")
print("-="*10)
peso = float(input("Informe seu peso (kg): "))
altura = float(input("Informe sua altura (m): "))
imc = peso/(altura*altura)

if imc < 18.5:
    print("Seu IMC é de {:.1f} \nVocê está abaixo do peso.".format(imc))
elif 18.5 <= imc < 25:
    print("Seu IMC é de {:.1f} \nVocê está no peso ideal.".format(imc))
elif 25 <= imc < 30:
    print("Seu IMC é de {:.1f} \nVocê está com sobrepeso.".format(imc))
elif 30 <= imc < 40:
    print("Seu IMC é de {:.1f} \nVocê está em obesidade. Cuidado!".format(imc))
elif imc >= 40:
    print("Seu IMC é de {:.1f} \nVocê está em obesidade mórbida. Cuidado!".format(imc))
