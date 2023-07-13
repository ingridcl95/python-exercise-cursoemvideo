#ler o comprimento de 3 retas e diga se pode ou não formar um triângulo
r1 = float("Digite o comprimento da primeira reta:")
r2 = float("Digite o comprimento da segunda reta:")
r3 = float("Digite o comprimento da terceira reta:")

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print("Essas retas podem formar um triângulo.")
else:
    print("Essas retas não podem formar um triângulo")
    