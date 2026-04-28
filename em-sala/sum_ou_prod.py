# Dado um numero inteiro n e uma opcao ambos inseridos pelo usuario
# se a opcao for 1, imprima o somatorio
# se a opcao for 2, imprima o produtorio

n = int(input("Insira um numero inteiro positivo: "))
opcao = int(input("Insira uma opcao: "))

if opcao == 1:
    soma = 0
    cont = 0 
    while cont <= n:
        soma += cont # soma = soma + cont
        cont += 1 # cont = cont + 1     
    print(f"Somatorio: {soma}")
elif opcao == 2:
    prod = 1
    cont = 1
    while cont <= n:
        prod *= cont # prod = prod * cont
        cont += 1 # cont = cont + 1
    print(f"Produtorio: {prod}")
else:
    print(f"Opcao {opcao} invalida")

print("Programa encerrado.")