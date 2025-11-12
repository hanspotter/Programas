# 🌌 Programa: Caça ao Tesouro Espacial 💎

# Cria o tabuleiro 3x3 (listas dentro de listas)
tabuleiro = [[" " for _ in range(3)] for _ in range(3)]

# Define a posição secreta do tesouro (linha e coluna)
tesouro_linha = 1
tesouro_coluna = 2

# Número máximo de tentativas
tentativas_max = 5

# Função para exibir o tabuleiro formatado
def mostrar_tabuleiro():
    print("\n🌍 Mapa do planeta misterioso:")
    for linha in tabuleiro:
        print(" | ".join(linha))
        print("-" * 9)

# Início do jogo
print("🚀 Bem-vindo à Caça ao Tesouro Espacial!")
print("Tente encontrar o 💎 escondido no planeta (linhas e colunas vão de 0 a 2).")

# Loop das tentativas
for tentativa in range(1, tentativas_max + 1):
    print(f"\nTentativa {tentativa} de {tentativas_max}")
    mostrar_tabuleiro()

    try:
        linha = int(input("Escolha a linha (0, 1 ou 2): "))
        coluna = int(input("Escolha a coluna (0, 1 ou 2): "))
    except ValueError:
        print("⚠️ Digite apenas números válidos!")
        continue

    # Verifica se está dentro dos limites
    if linha not in [0, 1, 2] or coluna not in [0, 1, 2]:
        print("🚫 Posição inválida! Use números entre 0 e 2.")
        continue

    # Verifica se já tentou esse espaço
    if tabuleiro[linha][coluna] in ["X", "💎"]:
        print("🌀 Você já tentou essa posição! Escolha outro lugar.")
        continue

    # Verifica se acertou o tesouro
    if linha == tesouro_linha and coluna == tesouro_coluna:
        tabuleiro[linha][coluna] = "💎"
        mostrar_tabuleiro()
        print("\n🎉 Incrível! Você encontrou o tesouro espacial! 💎✨")
        break
    else:
        tabuleiro[linha][coluna] = "X"
        print("❌ Nada aqui... continue procurando!")

# Se não encontrou depois de todas as tentativas
else:
    print("\n😢 Suas tentativas acabaram!")
    print(f"O tesouro estava na posição: linha {tesouro_linha}, coluna {tesouro_coluna}.")
    tabuleiro[tesouro_linha][tesouro_coluna] = "💎"
    mostrar_tabuleiro()
    print("👾 Boa sorte na próxima exploração!")

