from time import sleep
nome = str(input("Digite seu nome completo: ")).strip()
print("\nAnalisando seu nome...")
sleep(3)
print(f"\nSeu nome em maiúsculas é {nome.upper()}") # O "upper" é usado para converter as letras para maiúsculas.
print(f"Seu nome em minúsculas é {nome.lower()}") # O "lower" é usado para converter as letras para minúsculas.
print(f"Seu nome tem ao todo {len(nome) - nome.count(' ')} letras.")

# O "count" é usado para contar, e neste exemplo, ele vai contar quantos espaços tem (' ')
# Após isso, ele vai ser subitraído com a leitura (len) do que eu adicionar em "nome"
# Aliás, antes da subitração ocorrer, a resposta já está montada; apenas é subtraída para não haver confusão entre caractere e espaço.