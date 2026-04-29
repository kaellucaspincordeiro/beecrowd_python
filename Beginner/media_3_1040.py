nota_1, nota_2, nota_3, nota_4 = map(float, input().split())

media_atual = (nota_1 * 2 + nota_2 * 3 + nota_3 * 4 + nota_4) / 10

print(f"Media: {media_atual:.1f}")

if media_atual >= 7.0:
    print("Aluno aprovado.")
elif media_atual < 5.0:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")

    nota_exame = float(input())

    print(f"Nota do exame: {nota_exame:.1f}")

    media_exame = (media_atual + nota_exame) / 2

    if media_exame >= 5.0:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {media_exame:.1f}")    