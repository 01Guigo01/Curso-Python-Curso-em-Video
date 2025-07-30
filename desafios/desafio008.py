"""

DESAFIO 008

Escreva um programa que leia um valor em metros e o exiba convertido em todas as principais unidades de medida métricas.

"""

import time # Pra dar aquele charme com pausas

print("=" * 50)
print("✨ CONVERSOR DE UNIDADES DE MEDIDA ✨".center(50)) # Título com toque especial
print("=" * 50)

meters = float(input("📏 Digite uma distância em metros (ex: 1500.75): "))

print(f"\nCalculando as conversões para \033[1;36m{meters:.2f} metros\033[m...") # Destaca a medida em ciano
time.sleep(2)

kilometers = meters / 1000
hectometers = meters / 100
decameters = meters / 10

decimeters = meters * 10
centimeters = meters * 100
millimeters = meters * 1000

print("\n" + "=" * 50)
print("📊 TABELA DE CONVERSÃO 📊".center(50)) # Título da tabela
print("=" * 50)

print(f"A medida de \033[1;36m{meters:.2f} metros\033[m corresponde a:")
print("-" * 50)

print(f"⬆️  \033[1;31m{kilometers:.3f} km\033[m (Quilômetros)")
print(f"⬆️  \033[1;31m{hectometers:.2f} hm\033[m (Hectômetros)")
print(f"⬆️  \033[1;31m{decameters:.1f} dam\033[m (Decâmetros)")

print("-" * 50) # Linha pra separar unidades maiores e menores

print(f"➡️  \033[1;33m{meters:.2f} m\033[m (Metros - Valor Original)")

print("-" * 50) # Linha pra separar unidades maiores e menores

print(f"⬇️  \033[1;32m{decimeters:.1f} dm\033[m (Decímetros)")
print(f"⬇️  \033[1;32m{centimeters:.0f} cm\033[m (Centímetros)")
print(f"⬇️  \033[1;32m{millimeters:.0f} mm\033[m (Milímetros)")

print("=" * 50)
print("CONVERSÕES CONCLUÍDAS!".center(50))
print("=" * 50)
