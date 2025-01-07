print("Gerador de PA")
print("=-=" * 10)
primeiro = int(input("Digite o primeiro termo: "))
razão = int(input("\nDigite a razão desta PA: "))

termo = primeiro
cont = 1 # Contador para acompanhar quantos termos foram exibidos até o momento, iniciando com 1.
total = 0 # Essa variável soma o número total de termos exibidos. Inicialmente, é 0.
mais = 10 # Armazena o número de termos que o usuário deseja mostrar. Começa com 10 (os 10 termos iniciais).

while mais != 0:
    total += mais #Se o usuário desejar mais números será somado com o total que já havia.
    while cont <= total:
        print(f"{termo} -> ", end="")
        termo += razão
        cont += 1
    print("PAUSA")
    mais = int(input("\nQuantos termos você quer mostrar a mais? "))

print(f"\nProgressão finalizada com {total} termos mostrados.")