from random import randint
from time import sleep #O import "sleep" é usado para dar uma pausa no programa

computador = randint (0, 5) #Faz o computador "PENSAR"

print("-=-" * 20) #Apenas para destacar
print("Vou pensar em um número entre 0 a 5. Tente adivinhar...")
print("-=-" * 20)
jogador = int(input("Em que número eu pensei? ")) #Jogador tenta adivinhar
print()
print("PROCESSANDO...")
sleep(3)
print()

if jogador == computador:
    print("PARABÉNS! Você conseguiu me vencer!")
else:
    print("GANHEI! Eu pensei no número {} e não no {}!".format(computador, jogador))