"""

Desafio067

Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.

"""
import time
import emoji

print("=" * 50)
print("✨ TABUADA MÁGICA INTERATIVA ✨".center(50))
print("Veja a tabuada de qualquer número que você quiser!".center(50))
print("=" * 50)

keep_going = 'S'

while keep_going == 'S':
    number = int(input("🔢 Digite um número para ver sua tabuada: "))

    print(f"\nCalculando a tabuada de \033[1;36m{number}\033[m...")
    time.sleep(1.5)

    print("\n" + "=" * 20 + f" TABUADA DE {number} " + "=" * 20)
    for i in range(0, 11):
        result = number * i
        print(f"    \033[1;33m{number}\033[m X \033[1;33m{i}\033[m = \033[1;32m{result}\033[m")
        time.sleep(0.2)
    print("=" * 50)

    keep_going_valid = False
    while not keep_going_valid:
        print("\n" + "=" * 50)
        keep_going = str(input("Quer ver a tabuada de outro número? [S/N]: ")).strip().upper()[0]
        print("=" * 50)
        if keep_going in "SN":
            keep_going_valid = True
        else:
            print("\n❌ Resposta inválida! Por favor, digite 'S' para Sim ou 'N' para Não.")
            time.sleep(1)

print("\n🎉 Volte sempre que precisar de uma tabuada mágica!")
print("=" * 50)
