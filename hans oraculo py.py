# 🔮 Oráculo da Sabedoria Python

print("🧙‍♂️ Bem-vindo ao Oráculo da Sabedoria Python!")
print("Pergunte sobre um tema da programação e eu te darei um conselho...\n")

assunto = input("👉 Sobre qual tema você quer saber? (ex: variáveis, loops, funções, listas, orientação a objetos): ").lower()

print("\n✨ Consultando o grande Oráculo...\n")

# Estrutura match-case (Python 3.10+)
match assunto:
    case "variáveis" | "variavel":
        print("💡 As variáveis são como caixinhas mágicas que guardam valores! Use nomes claros e cuide bem delas. 🧰")
    case "loops" | "laços" | "repetição":
        print("🔁 Os loops te dão poder infinito... mas cuidado para não cair em um loop sem fim! ⏳")
    case "funções" | "def":
        print("🧠 As funções são feitiços poderosos — definidas uma vez, usadas muitas! Domine-as e dominará o código. 🪄")
    case "listas" | "arrays":
        print("📜 As listas guardam tesouros em ordem. Cada item tem seu lugar... e cada índice, seu segredo. 💎")
    case "orientação a objetos" | "poo":
        print("🏛️ A orientação a objetos é a arte de pensar como um criador — classes, heranças e métodos moldam mundos inteiros! 🌍")
    case _:
        print("🤖 Hmmm... esse tema ainda é um mistério para mim. Estou aprendendo novas magias de programação todos os dias! 🔮")
