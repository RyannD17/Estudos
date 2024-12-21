primeiro = int(input("Digite o primeiro termo: "))
razão = int(input("\nDigite a razão desta PA: "))
print()
print("PA:")
décimo = primeiro + (10 - 1) * razão

for cont in range(primeiro, décimo + razão, razão):
    print(f"{cont}", end = " -> ")

print("Acabou-se!")