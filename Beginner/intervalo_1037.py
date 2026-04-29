numero_intervalo = float(input())

if 0 <= numero_intervalo <= 25:
    print("Intervalo [0,25]")
elif 25 < numero_intervalo <= 50:
    print("Intervalo (25,50]")
elif 50 < numero_intervalo <= 75:
    print("Intervalo (50,75]")
elif 75 < numero_intervalo <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")
    