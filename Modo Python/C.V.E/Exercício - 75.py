num = (int(input("Digite um número: ")),
       int(input("Digite outro número: ")),
       int(input("Digite mais um número: ")),    
       int(input("Agora no sério, digite o último número: ")))

print(f"\nVocê digitou os valores {num}")
      
if num.count(9) == 1:
    print("O valor 9 apareceu uma vez.")
elif num.count(9) > 1:
    print(f"O valor 9 apareceu {num.count(9)} vezes.")
else:
    print("O valor 9 não apareceu uma única vez.")

if 3 in num:
    print(f"O valor 3 aparece na {num.index(3) + 1}ª posição.")
else:
    print("O valor 3 não foi digitado em nenhuma posição.")

print("Os valores pares digitados foram: ", end="")
for n in num:
    if n % 2 == 0:
        print(n, end=" ")