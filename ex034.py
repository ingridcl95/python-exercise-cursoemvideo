#ler um salário e calcular um aumento. se o salário for superior a 1.250, aumento de 10%, menor que isso, 15%
salario = float(input("Digite o valor do salário atual:"))
print("--- Calculando reajuste, aguarde...---")
if salario <= 1250:
    reajuste = salario*(15/100)
    print("O seu novo salário com 15% de aumento é R$ {:.2f}".format(salario+reajuste))
else:
    reajuste = salario*(10/100)
    print('O seu novo salário com 10% de aumento é R$ {:.2f}'.format(salario + reajuste))
