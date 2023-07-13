#faça um algoritmo que leia uma temperada em graus Celsius e converta para farenhait
tc = float(input('Digite a temperatura: ºC'))
f = (tc*1.8)+32
print('A temperatura de {} ºC corresponde a {}ºF'.format(tc, f))