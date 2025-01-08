#Questão: Escreva um programa leia dois nomes de times de futebol, a quantidade de gols do primeiro time, a quantidade de gols do segundo time e mostre o nome do time vencedor da partida.

time_1 = input("Digite o nome do primeiro time: ")
gols_time_1 = int(input("Quantos gols o {} fez no jogo? ".format(time_1)))
print()

time_2 = input("Digite o nome do segundo time: ")
gols_time_2 = int(input("Quantos gols o {} fez no jogo? ".format(time_2)))
print()

if gols_time_1 > gols_time_2:
    print("O {} venceu a partida contra o {} com o placar de {}x{}!".format(time_1, time_2, gols_time_1, gols_time_2))

elif gols_time_1 < gols_time_2:
    print("O {} venceu a partida contra o {} com o placar de {}x{}!".format(time_2, time_1, gols_time_2, gols_time_1))

else:
    print("O {} empatou contra o {} com o placar de {}x{}!".format(time_1, time_2, gols_time_1, gols_time_2))