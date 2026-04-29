a, b, c, d = map(int, input().split())

valores_aceitos = (
    b > c 
    and d > a 
    and c + d > a + b 
    and c > 0 
    and d > 0 
    and a % 2 == 0
)

if valores_aceitos:
    print(f"Valores aceitos")
else:
    print(f"Valores nao aceitos") 
