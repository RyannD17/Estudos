#Questão: Faça um Programa que leia três números e mostre o maior deles.

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))

#Verificando quem é maior
maior = a #Aqui estou destacando que "a" é a variável com MAIOR valor

if b > a and b > c:
    maior = b #Já neste estou destacando que "b" passará como o maior valor SE "a" e "c" forem inferiores

if c > a and c > b:
    maior = c #Retomando a ideia, ultilizo a mesma tática com a variável "c", ou seja: "c" passará a ser o maior valor

print("\nO maior valor é {}".format(maior))