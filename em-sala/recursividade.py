
def contagem(n):
    if n == 0:
        print("Fim")
    else:
        print(n)
        contagem(n - 1)

contagem(4)
