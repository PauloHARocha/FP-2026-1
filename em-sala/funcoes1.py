# criar uma funcao chamada "mensagem" que imprime o texto "Olá"

def saudacao(nome):
    print(f"Olá {nome}, tudo bem?")

def soma(a, b):
    print(a + b)

saudacao("Carlos")
saudacao("Paulo")
saudacao("Ana")

soma(10, 20)

def escopo():
    x = 10
    print(x)

escopo()

mensagem = "Python"

def imprime():
    mensagem = "Java"
    print(mensagem)

imprime()
print(mensagem)

def soma(a, b):
    return a + b

n1 = int(input())
n2 = input()
n2 = int(n2)

resultado = soma(n1, n2)
print(f"Resultado = {resultado}")

def quadrado(x):
    x = x**2
    return x

print(quadrado(10))


