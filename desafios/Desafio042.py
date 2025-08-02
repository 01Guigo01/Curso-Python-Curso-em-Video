"""

Desafio 042

Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- Equilátero: Todos os lados iguais.

- Isósceles: Dois lados iguais.

- Escleno: todos os lados diferente.

"""

import time

print("=" * 50)
print("✨ CONSTRUTOR E CLASSIFICADOR DE TRIÂNGULOS ✨".center(50))
print("=" * 50)

print("Por favor, digite os comprimentos de três segmentos de reta.")
print("Vamos verificar se eles podem formar um triângulo e, em caso positivo, que tipo de triângulo é.")

segmento_a = float(input("Digite o comprimento do 1º segmento: "))
segmento_b = float(input("Digite o comprimento do 2º segmento: "))
segmento_c = float(input("Digite o comprimento do 3º segmento: "))

print("\nAnalisando os segmentos...")
time.sleep(2)

print("-" * 50)
print(f"Segmentos informados: A={segmento_a:.2f}, B={segmento_b:.2f}, C={segmento_c:.2f}")
print("-" * 50)

if (segmento_a < segmento_b + segmento_c and
    segmento_b < segmento_a + segmento_c and
    segmento_c < segmento_a + segmento_b):

    print("\n✅ Ótima notícia! Os segmentos INFORMADOS PODEM FORMAR um triângulo!")
    time.sleep(1)

    print("\nAgora, vamos identificar o tipo de triângulo:")
    time.sleep(1)

    if segmento_a == segmento_b and segmento_b == segmento_c:
        print("    -> Este será um triângulo: \033[1;32mEQUILÁTERO\033[m (Todos os lados são iguais! 🎉)")
    elif segmento_a == segmento_b or segmento_a == segmento_c or segmento_b == segmento_c:
        print("    -> Este será um triângulo: \033[1;33mISÓSCELES\033[m (Dois lados são iguais! 🌟)")
    else:
        print("    -> Este será um triângulo: \033[1;34mESCALENO\033[m (Todos os lados são diferentes! 🚀)")

else: # Se a condição inicial de triângulo não for atendida
    print("\n❌ Lamento! Os segmentos INFORMADOS NÃO PODEM FORMAR um triângulo.")
    print("Para formar um triângulo, a soma de quaisquer dois lados deve ser maior que o terceiro lado.")

print("\n" + "=" * 50)
print("ANÁLISE DE TRIÂNGULOS CONCLUÍDA!".center(50))
print("=" * 50)
