
"""Leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços"""
print("\033[33m=*\033[m"*12)
print("DETECTOR DE PALÍNDROMOS")
print("\033[33m=*\033[m"*12)

frase = str(input("Digite uma frase: ")).strip().upper() #eliminei os espaços desnecessários e transformei em maiuscula
palavras = frase.split() #separei em palavras 'listas'
junto = "".join(palavras)  #juntei as palavras desconsiderando os espaços, pois deixei o parametro vazio
inverso = ""
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
print("O inverso de {} é {}.".format(junto, inverso))
if inverso == junto:
    print("Temos um \033[34mPALÍNDROMO\033[m.")
else:
    print("Não é um Palíndromo.")

"""INVERTENDO SEM O FOR
inverso = junto[::-1]
Utilizando o fatiamento, não informa início ou fim, então todos os caracteres são lidos e com o -1 será
de forma reversa"""
