times = ("Corinthians", "Palmeiras", "Santos", "Grêmio", "Cruzeiro", "Flamengo", "Vasco", "Chapecoense",
         "Atlético", "Botafogo", "Atlético-PR", "Bahia", "São Paulo", "Fluminense", "Sport Recife", "EC Vitória",
         "Coritiba", "Avaí", "Ponte Preta", "Atlético-GO")

print("-=-" * 15)
print("Lista de times do Brasileirão:")
print()
for t in times:
    print(t)

print("-=-" * 30)
print(f"Os 5 primeiro são: {times[0:5]}")
print("-=-" * 30)
print(f"Os 4 úçtimos são: {times[-4:]}")
print("-=-" * 30)
print(f"Times em ordem alfabética: {sorted(times)}")
print("-=-" * 30)
print(f"O Chapecoense está na {times.index('Chapecoense') + 1}ª posição.")

# Explicação:
# Quando adicionamos "times[0:5]" usa fatiamento para selecionar os 5 primeiros times da tupla times. Mas o índice final 5 não é incluído, exibindo 5 times.
# Quando adicionamos "times[-4:]" usa índices negativos para fatiar a tupla a partir dos 4 últimos elementos;
# A partir do final, a ausência de um valor após o ":" indica que pega até o último elemento.
# E por fim, a função "index('Chapecoense')" retorna o índice onde o time "Chapecoense" aparece na tupla.