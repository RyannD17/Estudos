from random import randint
itens = ("Pedra", "Papel", "Tesoura")
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')

jogador = int(input("\nQual a sua jogada? "))

print("-=" * 11)
print(f"Computador jogou {itens[computador]}")
print(f"Jogador jogou {itens[jogador]}")
print("-=" * 11)

if computador == 0:
    if jogador == 0:
        print("EMPATOU!")
    elif jogador == 1:
        print("JOGADOR VENCE!")
    elif jogador == 2:
        print("COMPUTADOR VENCE!")

    else:
        ("JOGADA INVÁLIDA!")

elif computador == 1:
    if jogador == 0:
        print("COMPUTADOR VENCE!")
    elif jogador == 1:
        print("EMPATOU!")
    elif jogador == 2:
        print("JOGADOR VENCE!")

    else:
        ("JOGADA INVÁLIDA!")

elif computador == 2:
    if jogador == 0:
        print("JOGADOR VENCE!")
    elif jogador == 1:
        print("COMPUTADOR VENCE!")
    elif jogador == 2:
        print("EMPATOU!")

    else:
        ("JOGADA INVÁLIDA!")