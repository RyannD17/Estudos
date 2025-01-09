#Questão: Escreva um programa que efetue a soma de dois arrays.

tamanho = int(input("Digite o tamanho dos arrays: "))

array1 = []
print("\nDigite os elementos do primeiro array:")
for i in range(tamanho):
    valor = int(input(f"Elemento {i+1}: "))
    array1.append(valor)

array2 = []
print("\nDigite os elementos do segundo array:")
for i in range(tamanho):
    valor = int(input(f"Elemento {i+1}: ")) # Pede ao usuário o valor para a posição "i".
    array2.append(valor)

array_soma = []
for i in range(tamanho):
    array_soma.append(array1[i] + array2[i])

print("\nArray resultante da soma:")
print(array_soma)

# Explicação:
# O laço "for i in range(tamanho):" se repete "tamanho" vezes, adicionado pelo usuário;
# O "valor = int(input(f'Elemento {i+1}: '))" pede ao usuário o valor para a posição "i";
# E também, adicionamos "{i+1}" porque o índice "i" começa em zero (já que na maioria das vezes contamos começando de 1);
# O "array_soma.append(array1[i] + array2[i])" é responsável pelas somas nos respectivos itens na lista (dado por [i])
    # Exemplo:
    # array1 = [2, 4, 6] | array2 = [1, 3, 5]
    # array1[0] + array2[0] = 2 + 1 = 3. E assim por diante para cada posição na lista.