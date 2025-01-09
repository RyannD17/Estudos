#Questão: Escreva um programa que leia duas palavras e mostre a quantidade de letras que aparecem nas duas palavras.

palavra_1 = str(input("Digite a primeira palavra: "))
palavra_2 = str(input("Digite a segunda palavra: "))

print(f"\nA quantidade de letras que aparecem na primeira palavra são {len(palavra_1)}.")
print(f"Já na segunda palavra, a quantidade de letras que aparecem são {len(palavra_2)}.")