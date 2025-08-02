"""

Desafio068

Faça um programa que jopgue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele constinou no final do jogo.

"""

import random
import time
import emoji

print("=" * 50)
print("✨ PAR OU ÍMPAR MÁGICO! ✨".center(50))
print("Jogue contra o computador até perder!".center(50))
print("=" * 50)

consecutive_wins = 0
keep_playing = True

while keep_playing:
    print("\n" + "-" * 50)
    print(f"PLACAR ATUAL: \033[1;32m{consecutive_wins}\033[m vitórias consecutivas!")
    print("-" * 50)

    player_choice_valid = False
    while not player_choice_valid:
        player_choice = str(input("Escolha Par ou Ímpar [P/I]: ")).strip().upper()[0]
        if player_choice in 'PI':
            player_choice_valid = True
        else:
            print("❌ Escolha inválida! Digite 'P' para Par ou 'I' para Ímpar.")
            time.sleep(1)

    player_number = int(input("Digite um número (0 a 10): "))

    computer_number = random.randint(0, 10)
    total = player_number + computer_number

    print("\nJO")
    time.sleep(0.5)
    print("KEN")
    time.sleep(0.5)
    print("PÔ!!!")
    time.sleep(0.7)

    print("-" * 50)
    print(f"Você jogou: \033[1;36m{player_number}\033[m")
    print(f"O computador jogou: \033[1;33m{computer_number}\033[m")
    print(f"A soma é: \033[1;34m{total}\033[m", end=" -> ")

    is_even = total % 2 == 0
    if is_even:
        print("É \033[1;34mPAR\033[m!")
    else:
        print("É \033[1;34mÍMPAR\033[m!")
    print("-" * 50)

    if (player_choice == 'P' and is_even) or (player_choice == 'I' and not is_even):
        print("\n🎉 VOCÊ VENCEU! Continue a sequência! 🎉")
        consecutive_wins += 1
        time.sleep(1.5)
    else:
        print("\n😢 VOCÊ PERDEU! A sequência de vitórias foi interrompida.")
        keep_playing = False
        time.sleep(1.5)

print("\n" + "=" * 50)
print("🏆 FIM DE JOGO! 🏆".center(50))
print("=" * 50)
print(f"Você conseguiu \033[1;33m{consecutive_wins}\033[m vitórias consecutivas!")
print(emoji.emojize(":partying_face: :trophy: :star-struck:"))
print("=" * 50)