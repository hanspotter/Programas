# Programa: Número Secreto 🎯

# Define o número secreto
numero_secreto = 7  

# Contador de tentativas
tentativas = 0  

# Laço para repetir até o jogador acertar
while True:
    chute = int(input("Adivinhe o número secreto (entre 1 e 10): "))
    tentativas += 1  # Soma +1 a cada tentativa

    if chute == numero_secreto:
        print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        break  # Sai do loop quando acerta
    elif chute < numero_secreto:
        print("🔼 O número secreto é maior. Tente novamente!")
    else:
        print("🔽 O número secreto é menor. Tente novamente!")
