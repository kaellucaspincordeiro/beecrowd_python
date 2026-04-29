hora_ini, minuto_ini, hora_final, minuto_final = map(int, input().split())

inicio = hora_ini * 60 + minuto_ini
fim = hora_final * 60 + minuto_final

duracao = fim - inicio

if duracao <= 0:
    duracao += 24 * 60

duracao_hora = duracao // 60
duracao_minuto = duracao % 60 
    
print(f"O JOGO DUROU {duracao_hora} HORA(S) E {duracao_minuto} MINUTO(S)")