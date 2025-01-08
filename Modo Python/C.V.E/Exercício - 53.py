frase = str(input("Digite uma frase: ")).strip().upper() # O "strip" serve para eliminar espaços antes e depois das frases que digitarei.

# Os espaços INTERNOS foram eliminados com o uso do código abaixo:
# ---------------------------
palavras = frase.split()  # |
junto = "".join(palavras) # |
# ---------------------------

inverso = ""

for letra in range(len(junto) - 1, -1, -1):
    print(junto[letra])
    inverso += junto[letra]

if inverso == junto:
    print("Temos um palíndromo!")
else:
    print("Não temos um palíndromo!")


# O que "range(len(junto) - 1, -1, -1)" faz? (Usaremos [P Y T H O N] como exemplo).
#                                                      [0 1 2 3 4 5] *POSIÇÕES*

# Esse comando cria uma sequência de números de trás para frente:

# "len(junto) - 1" é o último índice (a posição 5 no exemplo).
# -1 é até onde vai (que é até o zero, mas sem incluir).
# -1 é o passo, ou seja, ele vai "andando para trás".

# Ficaria dessa forma agora: N O H T Y P
#                           [5 4 3 2 1 0] *POSIÇÕES*