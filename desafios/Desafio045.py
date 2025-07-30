import random
import time

print("=" * 50)
print("✨ JOKENPÔ: PEDRA, PAPEL E TESOURA ✨".center(50))
print("=" * 50)

placar_jogador = 0
placar_computador = 0
rodadas_jogadas = 0

while True: # Loop principal do jogo
    rodadas_jogadas += 1
    print(f"\n--- RODADA {rodadas_jogadas} ---")
    print(f"PLACAR ATUAL: Você {placar_jogador} x {placar_computador} Computador")

    opcoes = {
        1: "PEDRA",
        2: "PAPEL",
        3: "TESOURA"
    }

    print("\nSuas opções:")
    print("[ 1 ] PEDRA")
    print("[ 2 ] PAPEL")
    print("[ 3 ] TESOURA")

    escolha_valida = False
    while not escolha_valida: # Loop para garantir uma escolha válida do jogador
        try:
            escolha_jogador_num = int(input("Qual é a sua jogada? (Digite o número): "))
            if escolha_jogador_num in opcoes:
                escolha_jogador_nome = opcoes[escolha_jogador_num]
                escolha_valida = True
            else:
                print("Opção inválida! Por favor, escolha 1, 2 ou 3.")
        except ValueError:
            print("Entrada inválida! Digite um número.")

    escolha_computador_num = random.randint(1, 3)
    escolha_computador_nome = opcoes[escolha_computador_num]

    print("\nJO")
    time.sleep(0.5)
    print("KEN")
    time.sleep(0.5)
    print("PÔ!!!")
    time.sleep(0.7)

    print("-" * 50)
    print(f"Você jogou: \033[1;36m{escolha_jogador_nome}\033[m")
    print(f"O Computador jogou: \033[1;33m{escolha_computador_nome}\033[m")
    print("-" * 50)

    if escolha_jogador_num == escolha_computador_num:
        print("\n\033[1;34mEMPATE!\033[m Ninguém pontuou nesta rodada. 🤝")
    elif (escolha_jogador_num == 1 and escolha_computador_num == 3) or \
         (escolha_jogador_num == 2 and escolha_computador_num == 1) or \
         (escolha_jogador_num == 3 and escolha_computador_num == 2):
        print("\n\033[1;32mVOCÊ GANHOU!\033[m Ponto para você! 🎉")
        placar_jogador += 1
    else:
        print("\n\033[1;31mVOCÊ PERDEU!\033[m Ponto para o Computador. 😢")
        placar_computador += 1

    time.sleep(1.5)

    # --- NOVO LOOP AQUI para perguntar se quer jogar novamente ---
    print("\n" + "=" * 50)
    resposta_valida = False
    while not resposta_valida:
        jogar_novamente = input("Quer jogar outra rodada? (S/N): ").upper().strip()
        if jogar_novamente == 'S':
            resposta_valida = True
        elif jogar_novamente == 'N':
            resposta_valida = True
        else:
            print("❌ Resposta inválida! Por favor, digite 'S' para Sim ou 'N' para Não.")
    print("=" * 50)

    if jogar_novamente == 'N':
        print("\nEntendido! Encerrando o jogo...")
        break # Sai do loop principal se a resposta for 'N'

# Fim do jogo - Declaração do vencedor
print("\n--- FIM DE JOGO ---")
print(f"PLACAR FINAL: Você {placar_jogador} x {placar_computador} Computador")

if placar_jogador > placar_computador:
    print("\n🏆 PARABÉNS! VOCÊ É O GRANDE VENCEDOR DO JOKENPÔ! 🏆")
elif placar_computador > placar_jogador:
    print("\n😔 QUE PENA! O COMPUTADOR VENCEU ESTA PARTIDA. Tente novamente!")
else:
    print("\n🤝 O JOGO TERMINOU EMPATADO! Que disputa acirrada!")

print("\n" + "=" * 50)
print("OBRIGADO POR JOGAR!".center(50))
print("=" * 50)
