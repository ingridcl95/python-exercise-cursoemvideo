#escreva um programa que leia a velocidade de um carro, se ultrapassar 80km/h mostre uma msg dizendo que foi multado
# a multa será de 7,00 a cada km acima do limite
print('--- VEJA SE VOCÊ FOI MULTADO! ---')
vel_carro = float(input('Em que velocidade você estava dirigindo?'))
if vel_carro > 80:
    print('Você foi multado! O limite permitido é de 80km/h!')
    multa = (vel_carro-80)*7
    print("Você deve pagar R$ {:.2f} de multa.".format(multa))
print()
print("Tenha um bom dia. Dirija com segurança!")
