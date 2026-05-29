
def soma(a, b):
    return a + b

def dobro(x):
    return x * 2

def operacao(valor1, valor2):
    d_valor1 = dobro(valor1)
    return soma(d_valor1, valor2)

x = 2
y = 10
resultado = soma(a=x, b=y)
print(resultado)
resultado = dobro(x=x)
print(resultado)
resultado = operacao(x, y)
print(resultado)

