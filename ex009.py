## escreva um algoritmo que leia um número inteiro qualquer e retorne sua tabuada.
n = int(input('Digite um número para saber sua tabuada: '))
contador = 0
print('-'*17)
print('A tabuada de {} é:'.format(n))
print('-'*17)

while (contador<=10):
    print('{} x {} = {}'.format(n, contador, contador * n))
    contador = contador + 1
