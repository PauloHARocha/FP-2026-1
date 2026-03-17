# checa maior numero 
# 1. recebe primeiro numero do usuario
# 2. recebe o segundo numero do usuario
# 3. checar se primeiro numero é maior
# 3.1 Se sim
    # 3.1.1 imprimir primeiro numero maior
# 3.2 Se nao
    # 3.2.1 checar se primeiro numero menor
        # 3.2.2 Se sim
            # imprimir segundo numero maior
        # 3.2.3 Se nao
            #  Imprimir numeros iguais 

num01 = float(input("Digite o primeiro numero:"))
num02 = float(input("Digite o segundo numero:"))

if num01 > num02:
    print("Primeiro numero maior")
elif num01 < num02:
    print("Segundo numero maior")
else:
    print("Numeros iguais")

print("Fim")




