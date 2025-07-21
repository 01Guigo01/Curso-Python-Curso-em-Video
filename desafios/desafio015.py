"""
DESAFIO 015

Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos quais
ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

"""

print("=" * 50)
print("ALUGUEL DE CARROS".center(50))
print("=" * 50)

# --- Lógica Principal ---

# Solicita as informações ao usuário.
# A função input() retorna um texto (string), por isso convertemos para os tipos numéricos adequados.
# int() para dias (número inteiro) e float() para quilômetros (pode ter decimais).
rented_days = int(input("Por quantos dias o carro foi alugado? "))
km_driven = float(input("Quantos Km foram rodados com o carro? "))

# Define os custos para facilitar a leitura e manutenção do código.
price_per_day = 60.00
price_per_km = 0.15

# Calcula o preço total somando o custo dos dias e o custo da quilometragem.
total_price = (rented_days * price_per_day) + (km_driven * price_per_km)

# Exibe o resultado final para o usuário.
# A f-string com ':.2f' formata o número para ter sempre duas casas decimais, ideal para moeda.
print("-" * 50)
print(f"O preço total a pagar pelo aluguel é de R$ {total_price:.2f}")
print("=" * 50)
