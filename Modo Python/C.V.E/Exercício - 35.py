print("Analisador de Triângulos")
print("-=-" * 20) #Apenas para destacar

r1 = float(input("Primeiro segmento: "))
print()
r2 = float(input("Segundo segmento: "))
print()
r3 = float(input("Terceiro segmento: "))
print()

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2: #Aqui estou determinando que para formar um triângulo o PRIMEIRO VALOR deve ser MENOR QUE A SOMA DO SEGUNDO E TERCEIRO VALOR! Do mesmo modo, vale para o segundo e terceiro valor
    print("Os segmentos acima PODEM FORMAR triângulo.")
else:
    print("Os segmentos acima NÃO PODEM FORMAR triângulo.")

