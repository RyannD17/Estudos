from time import sleep
print("Gerador de PA")
print("=-=" * 10)
primeiro = int(input("Digite o primeiro termo: "))
razão = int(input("\nDigite a razão desta PA: "))

termo = primeiro
cont = 1 # O contador iniciará no 1 e será usado para contar os 10 termos gerados.

print("=-=" * 10)
print("Gerando sua PA:")
sleep(2)

while cont <= 10:
    print(f"{termo} -> ", end="")
    termo += razão
    cont += 1
print("FIM")