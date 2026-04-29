valor_centavos = round(float(input()) * 100)

nota_100 = valor_centavos // 10000
valor_centavos %= 10000

nota_50 = valor_centavos // 5000
valor_centavos %= 5000

nota_20 = valor_centavos // 2000
valor_centavos %= 2000

nota_10 = valor_centavos // 1000
valor_centavos %= 1000

nota_5 = valor_centavos // 500
valor_centavos %= 500

nota_2 = valor_centavos // 200
valor_centavos %= 200

moeda_1 = valor_centavos // 100
valor_centavos %= 100

moeda_50 = valor_centavos // 50
valor_centavos %= 50

moeda_25 = valor_centavos // 25
valor_centavos %= 25

moeda_10 = valor_centavos // 10
valor_centavos %= 10

moeda_5 = valor_centavos // 5
valor_centavos %= 5

moeda_1_centavo = valor_centavos

print(f"NOTAS:")
print(f"{nota_100} nota(s) de R$ 100.00")
print(f"{nota_50} nota(s) de R$ 50.00")
print(f"{nota_20} nota(s) de R$ 20.00")
print(f"{nota_10} nota(s) de R$ 10.00")
print(f"{nota_5} nota(s) de R$ 5.00")
print(f"{nota_2} nota(s) de R$ 2.00")
print(f"MOEDAS:")
print(f"{moeda_1} moeda(s) de R$ 1.00")
print(f"{moeda_50} moeda(s) de R$ 0.50")
print(f"{moeda_25} moeda(s) de R$ 0.25")
print(f"{moeda_10} moeda(s) de R$ 0.10")
print(f"{moeda_5} moeda(s) de R$ 0.05")
print(f"{moeda_1_centavo} moeda(s) de R$ 0.01")