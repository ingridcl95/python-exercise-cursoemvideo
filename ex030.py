#ler um número inteiro informado pelo usuário e informe se é par ou impar
numero = int(input('Digite um número:'))
print('-'*17)
resultado = numero % 2
if resultado == 0:
    print('Este número é PAR.')
else:
    print('Este número é ÍMPAR.')
