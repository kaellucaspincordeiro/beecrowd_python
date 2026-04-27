_, qtd1, preco1 = input().split() 
_, qtd2, preco2 = input().split() 


qtd1 = int(qtd1)
preco1 = float(preco1)
qtd2 = int(qtd2)
preco2 = float(preco2)

total = qtd1 * preco1 + qtd2 * preco2

print(f"VALOR A PAGAR: R$ {total:.2f}")