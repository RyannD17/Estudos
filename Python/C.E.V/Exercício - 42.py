# Retomando o "Exercício - 35"
print("Analisador de Triângulos")
print("-=-" * 20) #Apenas para destacar

r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f"\nOs segmentos acima PODEM FORMAR um triângulo ", end=(""))
    if r1 == r2 == r3:
        print("EQUILÁTERO!")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO!")
    else:
        print("ISÓSCELES!")

else:
    print("\nOs segmentos acima NÃO PODEM FORMAR um triângulo!")