"""

Desafio 046

Façc um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifícios, indo de 10 até 0,
com uma pausa de 1 segundo entre eles.

"""

import time
import emoji

print("=" * 50)
print("✨ CONTAGEM REGRESSIVA! ✨".center(50))
print("Preparar, apontar, VAI!".center(50))
print("=" * 50)

start = int(input("🔢 Em qual número deseja iniciar?: "))
end = int(input("🔢 Em qual número deseja acabar: "))
something = str(input(
    f"✍️ Digite algo ou aperte ENTER para começar a contagem de \033[1;36m{start}\033[m até \033[1;36m{end}\033[m: "))

print("\n" + "=" * 50)
print("INICIANDO A CONTAGEM...".center(50))
print("=" * 50)

for c in range(start, end - 1, -1):
    print(f"💥 {c} 💥")
    time.sleep(1)

print("\n" + "=" * 50)
print("🚀 FIM DA CONTAGEM! 🚀".center(50))
print("AÇÃO EXECUTADA!".center(50))
print("=" * 50)
