codigo_produto , quantidade = map(int, input().split())

if codigo_produto == 1:
    total = quantidade * 4.00
elif codigo_produto == 2:
    total = quantidade * 4.50
elif codigo_produto == 3:
    total = quantidade * 5.00
elif codigo_produto == 4:
    total = quantidade * 2.00
else:
    total = quantidade * 1.50

print(f"Total: R$ {total:.2f}")