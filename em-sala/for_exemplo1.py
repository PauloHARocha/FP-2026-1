#  Contar quantas vogais existem no texto
texto = "palavra"
contador = 0
for c in texto:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
        contador = contador + 1 # contador += 1

print(f"O texto tem {contador} vogais")
