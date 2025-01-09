#Questão: Um determinado material radioativo perde metade de sua massa a cada 50 segundos. Dada a massa inicial, em gramas, desenvolva um algoritmo que determine o tempo necessário para que a massa se torne menor que 0,5 grama. O algoritmo deve mostrar a massa inicial, a final e o tempo calculado mostrado na forma de horas, minutos e segundos.

massa_inicial = float(input("Digite a massa inicial em gramas: "))
massa = massa_inicial
tempo_total = 0  # Em segundos.

while massa >= 0.5:
    massa /= 2  # A massa diminui pela metade, como foi dito.
    tempo_total += 50  # Cada ciclo dura 50 segundos.

# Convertendo o tempo total para horas, minutos e segundos:
horas = tempo_total // 3600 # Os segundos totais das horas.
minutos = (tempo_total % 3600) // 60
segundos = tempo_total % 60

print(f"\nMassa inicial: {massa_inicial} gramas.")
print(f"Massa final: {massa:.4f} gramas.")
print(f"\nTempo total: {horas} horas, {minutos} minutos e {segundos} segundos.")