"""

Desafio058

Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o jogador vai
tentar adivinhar até acertar, mostrando no final quantos palpites foram necessário para vencer.

"""

import random
import time
import emoji

print("=" * 50)
print("✨ JOGO DE ADIVINHAÇÃO MÁGICA ✨".center(50))
print("Será que você consegue ler a minha mente?".center(50))
print("=" * 50)

computer_choice = random.randint(0, 10)
player_guess = -1
guesses = 0

print("\n🤯 Estou pensando em um número entre 0 e 10...")
time.sleep(2)

while player_guess != computer_choice:
    player_guess = int(input("🤔 Qual é o seu palpite? (Digite um número): "))

    guesses += 1

    if player_guess < computer_choice:
        print("➡️ Um pouco mais! Tente um número MAIOR.")
    elif player_guess > computer_choice:
        print("⬅️ Um pouco menos! Tente um número MENOR.")

print("\n" + "=" * 50)
print("🏆 VITÓRIA! 🏆".center(50))
print("=" * 50)
print(f"O número secreto era \033[1;32m{computer_choice}\033[m.")
print(f"Você precisou de \033[1;33m{guesses}\033[m palpites para vencer!")
print(emoji.emojize(":partying_face: :trophy: :star-struck:"))
print("=" * 50)
