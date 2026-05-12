# Maria acabou de iniciar seu curso de graduação na faculdade de medicina 
# e precisa de sua ajuda para organizar os experimentos de um laboratório 
# o qual ela é responsável. Ela quer saber no final do ano, quantas cobaias 
# foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.
# Este laboratório em especial utiliza três tipos de cobaias: sapos, ratos e coelhos. 
# Para obter estas informações, ela sabe exatamente o número de experimentos que foram realizados, 
# o tipo de cobaia utilizada e a quantidade de cobaias utilizadas em cada experimento.

# Entrada

# A primeira linha de entrada contém um valor inteiro N que indica os vários casos de teste
# que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) 
# que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'), 
# indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).

# Saída

# Apresente o total de cobaias utilizadas, o total de cada tipo de cobaia utilizada e o
# percentual de cada uma em relação ao total de cobaias utilizadas, sendo que o percentual 
# deve ser apresentado com dois dígitos após o ponto.

n = int(input())

quantia_C = 0
quantia_R = 0
quantia_S = 0
for i in range(n):
    quantia, tipo = input().split()
    quantia = int(quantia)
    if quantia > 15:
        quantia = 15
    
    if tipo == "C":
        quantia_C = quantia_C + quantia # quantia_C += quantia
    elif tipo == "R":
        quantia_R = quantia_R + quantia # quantia_R += quantia
    elif tipo == "S":
        quantia_S = quantia_S + quantia # quantia_S += quantia

quantia_total = quantia_C + quantia_R + quantia_S
print(f"Total: {quantia_total} cobaias")

print(f"Total de coelhos: {quantia_C}")
print(f"Total de ratos: {quantia_R}")
print(f"Total de sapos: {quantia_S}")


percentual_C = quantia_C/quantia_total*100
print(f"Percentual de coelhos: {percentual_C:.2f} %")
print(f"Percentual de ratos: {(quantia_R/quantia_total*100):.2f} %")
print(f"Percentual de sapos: {quantia_S/quantia_total*100:.2f} %")
