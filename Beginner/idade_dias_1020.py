dias_total = int(input())

anos = dias_total // 365
resto = dias_total % 365

meses = resto // 30
dias = resto % 30

print(f"{anos} ano(s)\n{meses} mes(es)\n{dias} dia(s)")