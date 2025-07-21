"""
DESESAFIO 021

Fa;ca um programa em Pyhton que abra e reproduza o áudio de um arquivo MP3

"""


import pygame
import time # Precisamos do 'time' para fazer o programa esperar

print("=" * 50)

print("MP3 LOUCOS".center(50))

# 1. Inicializa todos os módulos do Pygame
pygame.init()

# 2. Inicializa o mixer (módulo de áudio) do Pygame
# Esta linha é crucial para que o áudio funcione!
pygame.mixer.init()

music = 'teste.mp3' # Certifique-se de que 'teste.mp3' está na mesma pasta do seu script

pygame.mixer.music.load(music)

print(f"\nReproduzindo: {music}")

# 3. Toca a música uma vez
pygame.mixer.music.play(1)

# 4. Faz o programa esperar enquanto a música toca
# 'pygame.mixer.music.get_busy()' retorna True enquanto a música está tocando.
while pygame.mixer.music.get_busy():
    time.sleep(1) # Espera 1 segundo para não usar muita CPU

print("\nReprodução concluída!")

# 5. Desinicializa o Pygame e o mixer para liberar os recursos
pygame.mixer.quit()
pygame.quit()

print("=" * 50)