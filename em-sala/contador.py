# Implementar um contador que imprime
# de 0 até um numero inteiro inserido pelo usuario

n = input("Insira um numero inteiro: ")
n = int(n)

cont = 0

while cont <= n:
    print(cont)
    cont += 1 

print("Programa encerrado")