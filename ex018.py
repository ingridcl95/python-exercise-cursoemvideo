#algoritmo que leia um ângulo qualquer e mostra o valor do seno, cosseno e tangente desse ângulo
import math
angulo = float(input('Digite o ângulo: '))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print('O valor do Seno do ângulo {} é {:.2f}.'.format(angulo,seno))
print('O valor do Cosseno do ângulo {} é {:.2f}'.format(angulo,cosseno))
print('O valor da Tagente do ângulo {} é {:.2f}'.format(angulo,tangente))
