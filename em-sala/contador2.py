# Implementar um contador que imprime
# de n até 1 sendo n um numero inteiro inserido pelo usuario

n = int(input("Insira um numero inteiro: "))

cont = n

while cont > 0: # cont >= 1
    print(cont)
    cont = cont - 1 # cont -= 1 

print(f"Programa encerrado para n = {n}")