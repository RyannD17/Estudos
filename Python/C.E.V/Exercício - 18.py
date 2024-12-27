import math
ângulo = float(input("Digite o valor do ângulo: "))

seno = math.sin(math.radians(ângulo)) # O ângulo será convertido para radiano e após isso, irá calcular seu seno.
print(f"\nO ângulo {ângulo} tem o seno de {seno:.2f}.")

cosseno = math.cos(math.radians(ângulo))
print(f"O ângulo {ângulo} tem o cosseno de {cosseno:.2f}.")

tangente = math.tan(math.radians(ângulo))
print(f"O ângulo {ângulo} tem a tangente de {tangente:.2f}.")