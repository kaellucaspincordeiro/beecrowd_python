tempo = int(input())
velocidade_media = int(input())

consumo_km_l = 12

litros = (tempo * velocidade_media) / consumo_km_l

print(f"{litros:.3f}")