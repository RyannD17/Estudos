#Questão: Escreva um programa que leia uma sequencia de nomes e mostre-os em ordem alfabética. O programa deve parar de ler quando o usuário digitar fim.

nomes = [] # Colchetes para LISTA!

print("Digite um nome para adicionar à lista. Se desejar encerrar, digite 'fim'.")

while True:
    nome = input("Digite um nome: ").strip()
    
    if nome.lower() == "fim":
        break
    
    nomes.append(nome) # Adicionamos os nomes na lista com o uso do ".append".

nomes.sort() # Usado para ordenar algo em uma lista. No caso das strings, ordena-se por ordem alfabética.

print("\nOs nomes em ordem alfabética são:")
for nome in nomes:
    print(nome)

# Explicação:
# O uso do "for nome in nomes" quer dizer: 
# "Para cada item da lista 'nomes', coloque esse item na variável 'nome' e faça o que está dentro do laço."