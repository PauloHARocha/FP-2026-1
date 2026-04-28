# Calcule a distância entre dois pontos no plano cartesiano. 
# Para isso, receba as coordenadas dos pontos (x1, y1) e (x2, y2) 
# e utilize a fórmula da distância euclidiana. 
# Exiba o valor da distância calculada.
import math

x1, y1 = map(float, input("Insira o ponto 1: ").split())
x2, y2 = map(float, input("Insira o ponto 2: ").split())

resultado = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

print(f"A distancia entre os pontos é {resultado:.2f}")
