# Contar quantos numeros pares numa sequencia
# dado um valor maximo 1 ate n

n = 20
contador = 0

for i in range(1, n):
    if i % 2 == 0:
        contador += 1 # contador = contador + 1

print(f"A sequencia tem {contador} numeros pares")