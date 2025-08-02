"""

Desafio 049 #TODO MELHORAR E COLOCAR LIMITE DE IDADE FAZER UMA GUI

Refaça o Desafio009, mostrando a tabuada de um número que o usuário escolher, só qaue agor utilizando um laço for.

"""

import time
import emoji

print("=" * 50)
print("✨ TABUADA MÁGICA: MULTIPLICAÇÃO TOTAL! ✨".center(50))
print("Descubra os segredos da sua tabuada.".center(50))
print("=" * 50)

num = int(input("🔢 Digite um número para ver a tabuada completa: "))
something = input(f"✍️ Digite algo ou aperte ENTER para começar a tabuada de \033[1;36m{num}\033[m: ")

print("\n" + "=" * 50)
print(f"TABUADA DO \033[1;36m{num}\033[m".center(50))
print("=" * 50)
time.sleep(1)

for c in range(1, 11):
    print(f"👉 \033[1;34m{num}\033[m x \033[1;34m{c:2}\033[m = \033[1;32m{num * c:3}\033[m")
    time.sleep(0.3)

print("\n" + "=" * 50)
print("🚀 FIM DA TABUADA! 🚀".center(50))
print("Obrigado por usar a nossa ferramenta!".center(50))
print("=" * 50)
