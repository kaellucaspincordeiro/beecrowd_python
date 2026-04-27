valor = int(input())

resto = valor

nota_100 = resto // 100
resto %= 100

nota_50 = resto // 50
resto %= 50

nota_20 = resto // 20
resto %= 20

nota_10 = resto // 10
resto %= 10

nota_5 = resto // 5
resto %= 5

nota_2 = resto // 2
resto %= 2

nota_1 = resto

print(f"{valor}")
print(f"{nota_100} nota(s) de R$ 100,00")
print(f"{nota_50} nota(s) de R$ 50,00")
print(f"{nota_20} nota(s) de R$ 20,00")
print(f"{nota_10} nota(s) de R$ 10,00")
print(f"{nota_5} nota(s) de R$ 5,00")
print(f"{nota_2} nota(s) de R$ 2,00")
print(f"{nota_1} nota(s) de R$ 1,00")