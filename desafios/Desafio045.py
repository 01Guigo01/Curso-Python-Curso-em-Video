"""

Desafio 045 #TODO MELHORAR E COLOCAR LIMITE DE IDADE FAZER UMA GUI

Faça um programa que jogue JOKENPO COM você

"""

import random
import time

print("=" * 50)
print("✨ JOKENPÔ: PEDRA, PAPEL E TESOURA ✨".center(50))
print("=" * 50)

import random
import time
import emoji

# Game variables
player_score = 0
computer_score = 0
rounds_played = 0
game_options = {
    1: "PEDRA",
    2: "PAPEL",
    3: "TESOURA"
}

print("=" * 50)
print("✨ JOKENPÔ MÁGICO: O DUELO FINAL! ✨".center(50))
print("Preparado para testar sua sorte?".center(50))
print("=" * 50)

while True:
    rounds_played += 1
    print(f"\n--- 🎲 RODADA {rounds_played} ---")
    print(f"PLACAR: Você \033[1;32m{player_score}\033[m x \033[1;31m{computer_score}\033[m Computador")

    print("\nEscolha sua arma secreta:")
    print("[ 1 ] PEDRA 🪨")
    print("[ 2 ] PAPEL 📄")
    print("[ 3 ] TESOURA ✂️")

    valid_choice = False
    while not valid_choice:
        try:
            player_choice_num = int(input("Qual é a sua jogada? (1, 2 ou 3): "))
            if player_choice_num in game_options:
                player_choice_name = game_options[player_choice_num]
                valid_choice = True
            else:
                print("❌ Opção inválida! Por favor, escolha 1, 2 ou 3.")
        except ValueError:
            print("❌ Entrada inválida! Digite um número.")

    computer_choice_num = random.randint(1, 3)
    computer_choice_name = game_options[computer_choice_num]

    print("\nJO")
    time.sleep(0.5)
    print("KEN")
    time.sleep(0.5)
    print("PÔ!!!")
    time.sleep(0.7)

    print("-" * 50)
    print(f"Você jogou: \033[1;36m{player_choice_name}\033[m")
    print(f"O Computador jogou: \033[1;33m{computer_choice_name}\033[m")
    print("-" * 50)

    if player_choice_num == computer_choice_num:
        print("\n\033[1;34mEMPATE!\033[m Ninguém pontuou nesta rodada. 🤝")
    elif (player_choice_num == 1 and computer_choice_num == 3) or \
         (player_choice_num == 2 and computer_choice_num == 1) or \
         (player_choice_num == 3 and computer_choice_num == 2):
        print("\n\033[1;32mVOCÊ GANHOU!\033[m Ponto para você! 🎉")
        player_score += 1
    else:
        print("\n\033[1;31mVOCÊ PERDEU!\033[m Ponto para o Computador. 😢")
        computer_score += 1

    time.sleep(1.5)

    print("\n" + "=" * 50)
    play_again_valid = False
    while not play_again_valid:
        play_again = input("Quer jogar outra rodada? (S/N): ").upper().strip()
        if play_again in ['S', 'N']:
            play_again_valid = True
        else:
            print("❌ Resposta inválida! Por favor, digite 'S' para Sim ou 'N' para Não.")
    print("=" * 50)

    if play_again == 'N':
        print("\nObrigado por jogar! Encerrando a partida...")
        break

print("\n--- 🏁 FIM DE JOGO 🏁 ---")
print(f"PLACAR FINAL: Você \033[1;32m{player_score}\033[m x \033[1;31m{computer_score}\033[m Computador")

if player_score > computer_score:
    print("\n🏆 PARABÉNS! VOCÊ É O GRANDE VENCEDOR! 🏆")
    print(emoji.emojize(":partying_face: :trophy: :star-struck:"))
elif computer_score > player_score:
    print("\n😔 QUE PENA! O COMPUTADOR TE DERROTOU. Tente novamente!")
    print(emoji.emojize(":robot: :unamused_face:"))
else:
    print("\n🤝 O JOGO TERMINOU EMPATADO! Que disputa acirrada!")
    print(emoji.emojize(":handshake: :neutral_face:"))

print("\n" + "=" * 50)
print("OBRIGADO POR JOGAR!".center(50))
print("=" * 50)
