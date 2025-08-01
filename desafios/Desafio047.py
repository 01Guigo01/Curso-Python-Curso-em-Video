"""

Desafio 047

Crie um programa que mosatre na tela todos os números pares que estãa no intervalo entre um número e outro

"""

import time
import emoji

print("=" * 50)
print("✨ EXPLORADOR DE NÚMEROS PARES! ✨".center(50))
print("Descubra os números pares em qualquer intervalo.".center(50))
print("=" * 50)

start = int(input("🔢 Em qual número deseja iniciar?: "))
end = int(input("🔢 Em qual número deseja acabar: "))

print(f"\nProcurando todos os números pares entre \033[1;36m{start}\033[m e \033[1;36m{end}\033[m...")
time.sleep(2)

print("\n" + "=" * 50)
print("🎉 RESULTADOS ENCONTRADOS 🎉".center(50))
print("=" * 50)

# The correct way to iterate and print only even numbers
print("Aqui estão os números pares:")
for n in range(start, end + 1):
    if n % 2 == 0:
        print(f"👉 \033[1;32m{n}\033[m")
        time.sleep(0.1)

print("\n" + "=" * 50)
print("BUSCA CONCLUÍDA!".center(50))
print("=" * 50)
