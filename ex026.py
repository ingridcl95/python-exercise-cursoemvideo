#Crie um programa que leia uma frase pelo teclado e mostre:
#Quantas vezes aparece a letra 'A'
#Em que posição ela aparece pela primeira vez
#Em que posição ela aparece pela última vez
frase = str(input('Digite uma frase:')).strip().upper()
print('-'*45)
print('A letra "A" aparece {} vezes na frase.'.format(frase.count('A')))
print('A primeira vez que a letra "A" aparece é na posição {}'.format(frase.find('A')))
#print('A primeira vez que a letra "A" aparece é na posição {}'.format(frase.find('A')+1))
#coloco o +1 para adequar a posição do caractere, com a primeira letra contando como índice 1
print('A última vez em que a letra "A" aparece é posição {}.'.format(frase.rfind('A')))
