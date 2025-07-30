""""

DESAFIO 009

Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

"""

import time

print("=" * 500)
print("✨ TABUADA MÁGICA PERSONALIZADA ✨".center(50))
print("=" * 50)


num_input = int(input("🔢 Digite o número que você quer ver a tabuada: "))

print(f"\nPreparando a tabuada do número \033[1;36m{num_input}\033[m...")
time.sleep(2)

print("\n" + "=" * 50)
print(f"📊 TABUADA DO {num_input:.2f} 📊".center(50))

print(f"👉 \033[1;34m{num_input:.2f}\033[m \033[1;33mx\033[m \033[1;34m 1\033[m \033[1;33m=\033[m \033[1;32m{num_input * 1}\033[m")

print(f"👉 \033[1;34m{num_input:.2f}\033[m \033[1;33mx\033[m \033[1;34m 2\033[m \033[1;33m=\033[m \033[1;32m{num_input * 2}\033[m")

print(f"👉 \033[1;34m{num_input:.2f}\033[m \033[1;33mx\033[m \033[1;34m 3\033[m \033[1;33m=\033[m \033[1;32m{num_input * 3}\033[m")

print(f"👉 \033[1;34m{num_input:.2f}\033[m \033[1;33mx\033[m \033[1;34m 4\033[m \033[1;33m=\033[m \033[1;32m{num_input * 4}\033[m")

print(f"👉 \033[1;34m{num_input:.2f}\033[m \033[1;33mx\033[m \033[1;34m 5\033[m \033[1;33m=\033[m \033[1;32m{num_input * 5}\033[m")

print(f"👉 \033[1;34m{num_input:.2f}\033[m \033[1;33mx\033[m \033[1;34m 6\033[m \033[1;33m=\033[m \033[1;32m{num_input * 6}\033[m")

print(f"👉 \033[1;34m{num_input:.2f}\033[m \033[1;33mx\033[m \033[1;34m 7\033[m \033[1;33m=\033[m \033[1;32m{num_input * 7}\033[m")

print(f"👉 \033[1;34m{num_input:.2f}\033[m \033[1;33mx\033[m \033[1;34m 8\033[m \033[1;33m=\033[m \033[1;32m{num_input * 8}\033[m")

print(f"👉 \033[1;34m{num_input:.2f}\033[m \033[1;33mx\033[m \033[1;34m 9\033[m \033[1;33m=\033[m \033[1;32m{num_input * 9}\033[m")

print(f"👉 \033[1;34m{num_input:.2f}\033[m \033[1;33mx\033[m \033[1;34m10\033[m \033[1;33m=\033[m \033[1;32m{num_input * 10}\033[m")

print("=" * 50)
print("TABUADA CONCLUÍDA!".center(50))
print("=" * 50)
