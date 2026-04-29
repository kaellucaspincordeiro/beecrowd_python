inicio, termino = map(int, input().split())


if inicio < termino:
    duracao = termino - inicio
else:
    duracao = 24 + termino - inicio
    
print(f"O JOGO DUROU {duracao} HORA(S)")