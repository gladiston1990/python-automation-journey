# DESAFIO (nível júnior)
#   Exercício 7 — Simulador de salário
#   Peça:	nome, salário e	percentual de aumento 

#   Mostre: Funcionário: João
#   Salário antigo: R$ 2000.00
#   Aumento: 10%
#   Novo salário: R$ 2200.00

nome = str(input("Diginite o nome do funcionário: "))
salario = float(input("Digite o atual salário do funcionario: "))
aumento = int(input("Digite a porcentagem de aumento do salário: "))

salario_aumentado = (salario + salario * aumento)

print(f"Funcionário: {nome} \n")
print(f"Salário Antigo: {salario}\n")
print(f"Almento: {aumento}% \n")
print(f"Novo salário: {salario_aumentado}")