"""

DESESAFIO 028

Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu.

"""

from random import randint
from time import sleep
import emoji

print("=" * 50)
print("✨ ADIVINHE O NÚMERO SECRETO! ✨".center(50))
print("Será que você consegue ler minha mente?".center(50))
print("=" * 50)

computer_choice = randint(0, 5)

player_name = str(input("👤 Qual é o seu nome, campeão(ã)? ")).strip().title()

player_choice_str = input(f"🤔 {player_name}, digite um número entre \033[1;36m0 e 5\033[m: ").strip()

if not player_choice_str.isdigit() or not (0 <= int(player_choice_str) <= 5):
    print("\n❌ Ah, não! Sua escolha não é válida. Por favor, digite um número inteiro entre 0 e 5.")
    print("O jogo será encerrado. Tente novamente!")
    print("=" * 50)
    exit()

player_choice = int(player_choice_str)

print("\n🤯 Estou pensando muito... Qual será o seu palpite?")
print("⏳ PENSANDO EM UM NÚMERO SECRETO...")
sleep(3) # Reduzi um pouco para não ficar muito longo

print("\n" + "=" * 50)
print("🎲 RESULTADO DO DUELO! 🎲".center(50))
print("=" * 50)

if player_choice == computer_choice:
    print(f"🎉 Parabéns, \033[1;32m{player_name}\033[m! Você ACERTOU! 🎉")
    print(f"O número que eu pensei foi realmente o \033[1;32m{computer_choice}\033[m!")
    print(emoji.emojize(":partying_face: :trophy: :star-struck:"))
else:
    print(f"😔 Que pena, \033[1;31m{player_name}\033[m! Não foi dessa vez. 🙁")
    print(f"Você escolheu o número \033[1;34m{player_choice}\033[m,")
    print(f"Mas o número SECRETO que eu pensei foi o \033[1;32m{computer_choice}\033[m.")
    print(emoji.emojize(":unamused_face: :sad_but_relieved_face: :thumbs_down:"))

print("=" * 50)
print("FIM DO JOGO DE ADIVINHAÇÃO!".center(50))
print("=" * 50)
