#ler a distância de uma viagem em km e calcular o preço da passagem, cobrando 0,50 por km até 200km e 0,45 para mais longas
print('--- CALCULE O VALOR DA DISTÂNCIA DE SUA VIAGEM ---')
distancia = float(input('Quantos km teve sua viagem ao total?'))
if distancia <= 200:
    print('O valor de sua passagem foi R$ {:.2f}'.format(distancia*0.50))
else:
    print('O valor de sua passagem foi R$ {:.2f}'.format(distancia*0.45))

#preco = distancia *0.50 if distancia <= 200 else distancia*0.45 (maneira simplificada/ternária)