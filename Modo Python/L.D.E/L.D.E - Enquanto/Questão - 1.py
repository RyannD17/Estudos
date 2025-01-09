#Questão: Escreva um programa que leia n números e mostre a soma dos mesmos. O programa deve parar de ler quando o usuário digitar -1.

soma = 0

print("Digite números para somar. Se desejar, digite -1 para encerrar.")
print()

while True: # Declarando que o loop é infinito com o uso do "True"
    numero = int(input("Digite um número: "))
    
    if numero == -1:
        break # Parando o "loop".
    
    soma += numero

print(f"\nA soma de todos os números é {soma}.")