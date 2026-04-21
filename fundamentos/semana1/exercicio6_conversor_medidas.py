#   Exercício 6 — Conversor de medidas
#   peça metros 
#   mostre: Centímetros: X e Milímetros: Y

metros = float(input("Digite quantos metros você quer converter: "))
centimetros = (metros * 100)
milimetros = (metros * 1000)

print(f" {metros} equivale a {centimetros} centímetros e {milimetros} milímetros")