# 🧠 Quiz de Perguntas e Respostas

print("🎯 Bem-vindo ao Quiz de Programação Python!\n")
print("Responda às perguntas e veja quantos pontos você consegue fazer!\n")

# Lista de perguntas e respostas [pergunta, resposta]
perguntas = [
    ["Qual comando usamos para exibir algo na tela?", "print"],
    ["Qual palavra-chave cria uma função em Python?", "def"],
    ["Como chamamos uma sequência de caracteres em Python?", "string"],
    ["Qual símbolo é usado para comentários em Python?", "#"],
    ["Qual estrutura repetitiva usamos com uma lista?", "for"]
]

# Variável para contar os acertos
acertos = 0

# Laço para percorrer todas as perguntas
for pergunta, resposta_correta in perguntas:
    resposta_usuario = input(f"❓ {pergunta}\n👉 Sua resposta: ").lower()

    if resposta_usuario == resposta_correta.lower():
        print("✅ Resposta correta!\n")
        acertos += 1
    else:
        print(f"❌ Resposta errada! A resposta certa era: {resposta_correta}\n")

# Mostra o resultado final
print("🏁 Fim do quiz!")
print(f"Você acertou {acertos} de {len(perguntas)} perguntas. 🏆")

# Mensagem personalizada
if acertos == len(perguntas):
    print("🎉 Incrível! Você é um verdadeiro mestre do Python! 🐍")
elif acertos >= 3:
    print("😎 Muito bem! Você está no caminho certo.")
else:
    print("🤔 Continue estudando, jovem aprendiz do código!")
