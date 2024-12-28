nota_1 = float(input("Digite sua primeira nota: "))
nota_2 = float(input("Digite sua segunda nota: "))

média = (nota_1 + nota_2) / 2

if média < 5:
    total = ("REPROVADO!")

elif média >= 5 and média < 7:
    total = ("em RECUPERAÇÃO!")

elif média >= 7:
    total = ("APROVADO!")

print(f"\nTirando {nota_1:.1f} e {nota_2:.1f}, a média das notas é {média:.1f}. Portanto, o aluno está {total}")