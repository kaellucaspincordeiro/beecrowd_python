salario = float(input())

if salario <= 400.00:
    taxa = 15
elif salario <= 800.00:
    taxa = 12
elif salario <= 1200.00:
    taxa = 10
elif salario <= 2000.00:
    taxa = 7
else:
    taxa = 4

reajuste = salario * taxa / 100
novo_salario = salario + reajuste

print(f"Novo salário: {novo_salario:.2f}")
print(f"Reajuste ganho: {reajuste:.2f}")
print(f"Em percentual: {taxa} %")

