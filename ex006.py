## criar um algoritmo que leia um número e mostre o seu dobro, seu triplo e sua raiz quadrada.
numero = int(input('Digite um número: '))
print(' O dobro de {} é {} \n O seu triplo é {} \n E sua raíz quadrada é igual a {:.2f}'.format(numero, (numero*2), (numero*3), pow(numero,(1/2))))
25