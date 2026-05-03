codigo_produto, qtd = map(int, input().split())

if codigo_produto == 1:
    preco = 4.00
elif codigo_produto == 2:
    preco = 4.50
elif codigo_produto == 3:
    preco = 5.00
elif codigo_produto == 4:
    preco = 2.00
else:
    preco = 1.50

total_pagar = qtd * preco

print(f"Total: R$ {total_pagar:.2f}")