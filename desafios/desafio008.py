"""
DESAFIO 008

Escreva um programa que leia um valor em metros e o exiba convertido em todas as principais unidades de medida métricas.

"""

meters = float(input("Digite uma distância em metros: "))

kilometers = meters / 1000
hectometers = meters / 100
decameters = meters / 10

decimeters = meters * 10
centimeters = meters * 100
millimeters = meters * 1000

# --- Apresentação da Tabela de Conversão ---
print("=" * 50)
print(f"A medida de {meters}m corresponde a:".center(50))
print("-" * 50)

print(f"{kilometers} km (Quilômetros)")
print(f"{hectometers} hm (Hectômetros)")
print(f"{decameters} dam (Decâmetros)")
print(f"{decimeters} dm (Decímetros)")
print(f"{centimeters} cm (Centímetros)")
print(f"{millimeters} mm (Milímetros)")

print("=" * 50)