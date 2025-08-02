"""

Desafio059

Crie um programa que leia dois valores e mostre um menu na tela:

[1] Somar
[2] Subtrair
[3] Maior
[4] Novos números
[5] Sair do Programa

"""

import time
import emoji

first_number = 0.0
second_number = 0.0
option = 0
print("=" * 50)
print("✨ CALCULADORA MÁGICA: MENU DE OPERAÇÕES ✨".center(50))
print("Selecione sua operação e veja a mágica acontecer!".center(50))
print("=" * 50)

print("\n🔢 Por favor, digite dois valores para começar:")
first_number = float(input("➡️ Primeiro valor: "))
second_number = float(input("⬅️ Segundo valor: "))

while option != 5:
    print("\n" + "=" * 50)
    print("O que você deseja fazer agora?".center(50))
    print(f"Valores atuais: \033[1;36m{first_number}\033[m e \033[1;36m{second_number}\033[m")
    print("-" * 50)
    print("[ 1 ] Somar ➕")
    print("[ 2 ] Subtrair ➖")
    print("[ 3 ] Maior Valor 🏆")
    print("[ 4 ] Novos números 🔄")
    print("[ 5 ] Sair do Programa 🚪")
    print("=" * 50)

    option = int(input("Escolha sua opção: "))

    if option == 1:
        sum_result = first_number + second_number
        print(
            f"\n✅ A soma entre \033[1;36m{first_number}\033[m e \033[1;36m{second_number}\033[m é: \033[1;32m{sum_result}\033[m")
    elif option == 2:
        subtract_result = first_number - second_number
        print(
            f"\n✅ A subtração entre \033[1;36m{first_number}\033[m e \033[1;36m{second_number}\033[m é: \033[1;32m{subtract_result}\033[m")
    elif option == 3:
        if first_number > second_number:
            print(f"\n✅ O maior valor é: \033[1;32m{first_number}\033[m")
        elif second_number > first_number:
            print(f"\n✅ O maior valor é: \033[1;32m{second_number}\033[m")
        else:
            print("\n🤝 Os dois valores são iguais!")
    elif option == 4:
        print("\n🔄 Preparando para novos números...")
        time.sleep(1)
        print("\n🔢 Por favor, digite dois novos valores:")
        first_number = float(input("➡️ Primeiro valor: "))
        second_number = float(input("⬅️ Segundo valor: "))
    elif option == 5:
        print("\n🚪 Saindo do programa... Até a próxima!")
        time.sleep(1)
    else:
        print("\n❌ Opção inválida! Por favor, escolha uma opção entre 1 e 5.")

    if option != 5:
        time.sleep(1.5)
