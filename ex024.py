#Crie um programa que leia o nome de uma cidade e diga se ela começa com a palavra SANTO
cidade = str(input('Digite o nome de uma cidade:')).strip()
print('-'*12)
#cidade = cidade.upper()
#divcidade = cidade.split()
#print('SANTO' in divcidade[0])

print(cidade[:5].upper() == 'SANTO')
#dei a quantidade de caracteres da palavra e pedi pra analisar se esse intervalo de 0:5 é igual a 'SANTO'
