"""

DESESAFIO 021 #TODO MELHORAR E COLOCAR LIMITE DE IDADE FAZER UMA GUI

Façaa um programa em Pyhton que abra e reproduza o áudio de um arquivo MP3.

"""

import pygame
import time

print("=" * 50)
print("🎧 MP3 MALUCO: SUA MÚSICA NO COMANDO! 🎶".center(50))
print("=" * 50)

pygame.init()
pygame.mixer.init()

music = 'teste.mp3' # Certifique-se de que 'teste.mp3' está na mesma pasta!

# Carrega a música. ATENÇÃO: Se o arquivo não existir, o programa vai travar aqui!
pygame.mixer.music.load(music)

print(f"\nPreparando para reproduzir: \033[1;36m{music}\033[m")
time.sleep(1.5)

print("\n🔊 TOCANDO AGORA! Divirta-se! 🚀")
pygame.mixer.music.play(1)


while pygame.mixer.music.get_busy():
    time.sleep(1)

print("\n⏹️ Reprodução concluída! Espero que tenha gostado. 🎉")

pygame.mixer.quit()
pygame.quit()

print("=" * 50)
print("MP3 MALUCO ENCERRADO!".center(50))
print("=" * 50)
