import math

x1 , y1 = map(float, input().split())
x2 , y2 = map(float, input().split())

distancia = math.hypot(x2 - x1, y2 - y1)

print(f"{distancia:.4f}")