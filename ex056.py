"""Ler o nome, idade, e sexo de 4 pessoas. Mostrar no final:
 a média de idade, o nome do homem mais velho e quantas mulheres tem menos de 20 anos."""
somaidade = 0
maioridadeh = 0
nomeh = ""
mulher20 = 0
for pessoa in range(1, 5):
    print("---- {}ª PESSOA ----".format(pessoa))
    nome = str(input("Nome:")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if pessoa == 1 and sexo in "Mm":
         maioridadeh = idade
         nomeh = nome
    if idade > maioridadeh and sexo in "Mm":
            maioridadeh = idade
            nomeh = nome
    if sexo in "Ff" and idade < 20:
         mulher20 += 1

mediaidade = somaidade/4
print("A média de idade do grupo é de {:.1f} anos.".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}.".format(maioridadeh, nomeh))
if mulher20 > 1:
    print("{} mulheres tem menos de 20 anos.".format(mulher20))
else:
    print("{} mulher tem menos de 20 anos.".format(mulher20))

