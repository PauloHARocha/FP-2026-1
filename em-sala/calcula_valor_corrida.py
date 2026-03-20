# Exercicio 0 - Calcular valor corrida
# Pseudocodigo
# 1. Receber qtd_km_percorridos
# 2. Definir taxa_fixa = 5
# 3. Definir taxa_km = 2
# 4. Calcular valor_corrida = taxa_fixa + taxa_km * qtd_km_percorridos
# 5. Se valor_corrida > 50 entao
#   5.1 imprimir "Corrida cara"
# 6. Senao
#   6.1 Imprimir "Corrida normal"  

qtd_km_percorridos = input("Inserir quantidade de km percorridos: ")
qtd_km_percorridos = float(qtd_km_percorridos)

taxa_fixa = 5
taxa_km = 2

valor_corrida = taxa_fixa + taxa_km*qtd_km_percorridos

if valor_corrida > 50:
    print("Corrida cara")
else:
    print("Corrida normal")