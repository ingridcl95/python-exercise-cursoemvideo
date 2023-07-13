"""Escreva um programa que leia um número inteiro e peça para o usuário escolher para qual base numérica ele será convertido
1 - binário, 2 - octal, 3 - hexadecimal"""
print("=-"*10)
print("CONVERSOR DE BASES")
print("=-"*10)
numero = int(input("Informe o número que deseja converter: "))
print("""Escolha a base de conversão: 
1 - Binário
2 - Octal 
3 - Hexadecimal""")
base = int(input("Sua opção: "))

if base == 1:
    print("O número {} convertido em Binário é {}".format(numero, bin(numero)[2:]))
elif base == 2:
    print("O número {} convertido em Octal é {}".format(numero, oct(numero)[2:]))
elif base == 3:
    print("O número {} convertido em Hexadecimal [e {}".format(numero, hex(numero)[2:]))
else:
    print("Opção inválida. Tente novamente.")
