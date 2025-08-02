"""

Desafio062

Melhore o Desafio061m perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele
disser que quer mostrar 0 termos.

"""

import time
import emoji

print("=" * 50)
print("✨ CALCULADORA DE PA DINÂMICA ✨".center(50))
print("Descubra os termos da sua PA de forma interativa!".center(50))
print("=" * 50)

first_term = int(input("🔢 Digite o PRIMEIRO termo da PA: "))
reason = int(input("➕ Digite a RAZÃO da PA: "))

print(
    f"\nCalculando os 10 primeiros termos da PA com primeiro termo \033[1;36m{first_term}\033[m e razão \033[1;36m{reason}\033[m...")
time.sleep(2)

print("\n" + "=" * 50)
print("📝 OS TERMOS DA PA SÃO: 📝".center(50))
print("=" * 50)

current_term = first_term
count = 1
total_terms = 10

while count <= total_terms:
    print(f"👉 {count}º termo: \033[1;32m{current_term}\033[m")
    current_term += reason
    count += 1
    time.sleep(0.3)

more_terms = 1  # Define um valor inicial para entrar no loop
while more_terms != 0:
    print("\n" + "=" * 50)
    more_terms = int(input("Quantos termos a mais você quer ver? (0 para sair): "))
    print("=" * 50)

    if more_terms > 0:
        print("\n📝 MOSTRANDO NOVOS TERMOS: 📝".center(50))
        for _ in range(more_terms):
            print(f"👉 {count}º termo: \033[1;32m{current_term}\033[m")
            current_term += reason
            count += 1
            time.sleep(0.3)
    elif more_terms < 0:
        print("\n❌ Valor inválido! Digite um número positivo ou 0 para sair.")

print("\n🚪 Encerrando o programa...")
time.sleep(1)

print("\n" + "=" * 50)
print("CÁLCULO CONCLUÍDO!".center(50))
print("=" * 50)
print(emoji.emojize(":partying_face: :money_bag:"))
print("=" * 50)