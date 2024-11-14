#Questão: Ler dois valores inteiros e imprimir o maior deles

a = int(input("Digite o primeiro número: "))
print()
b = int(input("Digite o segundo número: "))
print()

if a > b:
    print("O primeiro número é o MAIOR!")
if b > a:
    print("O segundo número é o MAIOR!")
if a == b:
    print("Ambos os números possuem o mesmo valor!")