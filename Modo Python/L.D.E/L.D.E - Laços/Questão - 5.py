#Questão: Escreva um programa que leia n notas e calcule a média da turma (soma das notas dividido por n). O programa deve então mostrar quantas notas estão acima da média calculada e quais são e mostrar quantas estão abaixo da média calculada e quais são.

# Assim como na questão anterior...
n = int(input("Digite o número de notas: "))

notas = []
print("\nDigite as notas:")
for i in range(n):
    nota = float(input(f"Nota {i+1}: "))
    notas.append(nota)

media = sum(notas) / n
acima_media = []
abaixo_media = []
igual_media = []

for nota in notas:
    if nota > media:
        acima_media.append(nota)
    elif nota < media:
        abaixo_media.append(nota)
    else:
        igual_media.append(nota)

print(f"\nMédia da turma: {media:.2f}.")
print(f"Notas acima da média ({len(acima_media)}): {acima_media};")
print(f"Notas abaixo da média ({len(abaixo_media)}): {abaixo_media};")
print(f"Notas iguais à média ({len(igual_media)}): {igual_media}.")