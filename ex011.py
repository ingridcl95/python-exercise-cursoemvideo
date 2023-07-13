##Algoritmo que leia a largura e a altura de uma parede em metros, calcule sua área e a quantidade
# de tinta necessária para pintá-la.Sabendo que cada litro de tinta pinta uma área de 2m quadrados.

altura = float(input('Altura da parede:'))
largura = float(input('Largura da parede'))
area = altura*largura

print('Para pintar uma área de {}m você precisará de {:.2f}L de tinta.'.format(area, area/2))