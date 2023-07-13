"""Escreva um programa que calcule o valor a ser pago em produto considerando seu valor e forma de pagamento:
a vista (dinheiro ou cheque): 10% de desconto
a vista no cartão: 5% de desconto
cartão até 2x: preço normal
cartão em 3x ou mais: 20% de juros"""

print("{:=^40}".format("LOJAS GUANABARA"))
#CENTRALIZA O NOME APÓS 40 ESPAÇOS
product = float(input("VALOR DA COMPRA R$: "))
print("FORMA DE PAGAMENTO ESCOLHIDA:")
payment = int(input("""1 - À VISTA (DINHEIRO OU CHEQUE)
2 - À VISTA NO CARTÃO (1x)
3 - CARTÃO 2X
4 - CARTÃO 3x OU MAIS
DIGITE A OPÇÃO: """))

if payment == 1:
    value_product = product - (product*(10/100))
elif payment == 2:
    value_product = product - (product*(5/100))
    print("Total a pagar: R$ {:.2f}".format(value_product))
elif payment == 3:
    print("Pagamento em 2x de R$ {:.2f} SEM JUROS. Total R$ {:.2f}".format((product/2), product))
elif payment == 4:
    parcelas = int(input("INFORME QUANTIDADE DE PARCELAS:"))
    value_product = product + (product*(20/100))
    valor_parcelas = value_product/parcelas
    print(("Pagamento em {}x R$ {:.2f}. \nTotal R$ {:.2f}".format(parcelas, valor_parcelas, value_product)))
else:
    value_product = 0
    print("Opção inválida de pagamento. Tente novamente.")

