"""

Desafio 053

Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

"""

import time
import emoji

print("=" * 50)
print("✨ VERIFICADOR DE PALÍNDROMOS ✨".center(50))
print("Será que sua frase pode ser lida de trás para frente?".center(50))
print("=" * 50)

phrase = str(input("✍️ Digite uma frase: ")).strip().upper()

print(f"\nAnalisando a frase '\033[1;36m{phrase.title()}\033[m'...")
time.sleep(2)

clean_phrase = phrase.replace(" ", "")
reversed_phrase = clean_phrase[::-1]

print("\n" + "=" * 50)
print("🔍 RESULTADO DA ANÁLISE 🔍".center(50))
print("=" * 50)

if clean_phrase == reversed_phrase:
    print(f"🎉 A frase digitada é um \033[1;32mPALÍNDROMO\033[m! ✨")
    print(f"Original: \033[1;34m{clean_phrase}\033[m")
    print(f"Invertida: \033[1;34m{reversed_phrase}\033[m")
    print(emoji.emojize(":star-struck: :partying_face:"))
else:
    print(f"😔 A frase digitada \033[1;31mNÃO\033[m é um palíndromo. 🙁")
    print(f"Original: \033[1;34m{clean_phrase}\033[m")
    print(f"Invertida: \033[1;34m{reversed_phrase}\033[m")
    print(emoji.emojize(":unamused_face:"))

print("\n" + "=" * 50)
print("ANÁLISE CONCLUÍDA!".center(50))
print("=" * 50)
