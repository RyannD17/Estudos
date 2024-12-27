from time import sleep
frase = str(input("Digite uma frase: ")).upper().strip()
print("\nAnalisando a frase...")
sleep(3)
print(f"\nA letra 'A' aparece {frase.count('A')} vezes na frase.")
print(f"\nA primeira letra 'A' apareceu na posição {frase.find('A') + 1}.")
print(f"A última letra 'A' apareceu na posição {frase.rfind('A') + 1}.")