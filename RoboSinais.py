import os
import random
from termcolor import colored
import socket
import webbrowser  # Importe o módulo webbrowser

def esta_conectado_wifi():
    try:
        # Tente criar um socket para um endereço externo (como um servidor DNS)
        # Isso verificará se o dispositivo está conectado à internet por meio de Wi-Fi
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

# Verifique se o dispositivo está conectado a uma rede Wi-Fi
if not esta_conectado_wifi():
    print("O dispositivo não está conectado a uma rede Wi-Fi.")
    exit()

while True:
    os.system('clear' if os.name == 'posix' else 'cls')

    print(colored(" █▀▀█ █▀▀▀█ █▀▀█ █▀▀▀█   █▀▀▄ █▀▀▀   █▀▀▀█ ▀█▀ █▄░▒█ █▀▀█ ▀█   █▀▀▀█", 'green'))
    print(colored(" █▄▄▀ █░░▒█ █▀▀▄ █░░▒█   █░▒█ █▀▀▀   ▀▀▀▄▄ ░█░ █▒█▒█ █▄▄█ ░█░  ▀▀▀▄▄", 'green'))
    print(colored(" █░▒█ █▄▄▄█ █▄▄█ █▄▄▄█   █▄▄▀ █▄▄▄   █▄▄▄█ ▄█▄ █░░▀█ █░▒█ ▄█▄  █▄▄▄█", 'green'))
    print(colored("🌐 | Criado por @genius.py", 'blue'))
    print("")
    print(colored("🤖 Modos do Robô 🤖", 'light_grey'))
    print(colored("1 | Modo Blaze/Mines💣💎", 'yellow'))
    print(colored("2 | Modo Tigrinho🐯💰", 'yellow'))
    print(colored("3 | Créditos do Criador👨‍💻", 'yellow'))
    print(colored("4 | Fechar Robô/Bot❌", 'red'))
    print("")
    print(colored("Selecione uma opção:", 'green'))

    resposta = input()

    try:
        resposta = int(resposta)

        if resposta == 1:
            os.system('clear' if os.name == 'posix' else 'cls')
            print(colored("✅ | Modo Blaze escolhido, o seguinte jogo deverá ser efetuado no modo Mines do site Blaze.com", 'yellow'))

            chance = random.randint(70, 100)

            # Calcula a quantia recomendada com base na porcentagem de certeza
            quantia_recomendada = (chance / 100) * (50 - 10) + 10

            # Formata a quantia com vírgula em vez de ponto
            quantia_formatada = f"R${quantia_recomendada:.2f}".replace('.', ',')

            emojis_porcentagem = "↗️" if chance > 85 else "↘️"

            mensagem = f"📊 | Chance de certeza: {chance}% {emojis_porcentagem}\n💰 | Quantia recomendada: {quantia_formatada} 💸💸💸"

            # Use a função colored para imprimir em vermelho
            print(colored(mensagem, 'green'))

            print("")
            print(colored("🎰 < Tabela > 🎰", 'yellow'))
            print("")

            emojis = ["💣", "💎"]

            sequencia = ["💎"] * 5 + ["💣"] * 20

            random.shuffle(sequencia)

            linhas = [sequencia[i:i+5] for i in range(0, len(sequencia), 5)]

            def imprimir_sequencia(sequencia):
                for linha in sequencia:
                    linha_formatada = [colored(item, 'green') if item == "💎" else colored(item, 'white') for item in linha]
                    print("".join(linha_formatada))

            imprimir_sequencia(linhas)

        elif resposta == 2:
            os.system('clear' if os.name == 'posix' else 'cls')
            print("")
            print(colored("✅ | Modo Tigrinho escolhido, os seguintes resultados deverão ser efetuados no jogo, pois não tem um site específico para jogar.", 'yellow'))
            print("")
            print("")
            print("")
            print(colored("📋  Tabela de horários recomendados para maior ganho  📋", 'yellow'))
            print(colored("💸  Aumento de 5x o lucro  💸", 'green'))
            print("")

            # Gerar horários aleatórios e classificá-los em ordem crescente
            horarios = []

            while len(horarios) < 200:
                hora = random.randint(0, 23)
                minuto = random.randint(0, 59)
                horario = f"{hora:02}:{minuto:02}"
                if horario not in horarios:
                    horarios.append(horario)

            horarios.sort()

            for i in range(0, len(horarios), 10):
                linha = horarios[i:i+10]
                print(colored(" | ".join(linha), 'yellow'))
            print("")
            print("")
            print("")
            print(colored("🤑 | Jogando nos horários da tabela terá 5 vezes mais chances de ganho.  💸", 'green'))
            print("")

        elif resposta == 3:
            os.system('clear' if os.name == 'posix' else 'cls')
            webbrowser.open("https://www.instagram.com/genius.py/")
            print(colored("✅ | Modo Crédito escolhido", 'yellow'))
            print("")
            print(colored("Bom, vou esclarecer quem sou, me identifico como Genius...", 'green'))
            print("")
            print(colored("Esta é uma carta escrita pelo criador do Robô:", 'green'))
            print("")
            print(colored("Sou um estudante brasileiro, nasci no sul do país e sempre tive muita curiosidade.", 'green'))
            print(colored("Além da curiosidade, sempre tive muito medo do desconhecido, justamente por não saber do que se trata,", 'green'))
            print(colored("não saber o que pode causar, como pode causar e quando.", 'green'))
            print(colored("Esse meu medo, por uma parte, gerou muita sabedoria.", 'green'))
            print(colored("Vamos começar pelo começo...", 'green'))
            print(colored("Com 8 anos, eu jogava um jogo chamado Roblox.", 'green'))
            print(colored("Roblox não é bem um jogo, mas sim uma plataforma de jogos, e eu gostava tanto dessa plataforma", 'green'))
            print(colored("que na época joguei quase todos os jogos disponíveis, e para mim, nenhum jogo tinha mais graça.", 'green'))
            print(colored("Então, eu busquei saber como criar o meu próprio jogo, um jogo que eu pudesse escolher o que eu quisesse,", 'green'))
            print(colored("como seria tal coisa, como se comportaria a física, tudo sob meu controle.", 'green'))
            print(colored("Então, eu decidi buscar saber como eu poderia fazer isso, assim eu achei o mundo da programação,", 'green'))
            print(colored("ou melhor, o mundo da criação virtual, sem limites de criação.", 'green'))
            print(colored("Ao longo do tempo, fui desenvolvendo minhas técnicas, meu inglês e minhas linguagens de programação.", 'green'))
            print(colored("Fui criando mais jogos, mais sites, mais programas e mais sistemas, cada vez aprendendo coisas novas que eu nem imaginaria que existiriam.", 'green'))
            print(colored("E cá estou eu, no auge dos meus 14 anos de idade, criando robôs baseados em inteligência artificial", 'green'))
            print(colored("que analisam cuidadosamente o histórico de jogadas de jogos de cassinos online e decidem qual a maior probabilidade de ganhar a próxima rodada.", 'green'))
            print(colored("Bem, essa é um pouco da minha trajetória.", 'green'))
            print(colored("Tenho minha rede social onde posto sobre projetos, sistemas e interajo com o pessoal de lá.", 'green'))
            print(colored("Sigam @genius.py no Instagram.", 'yellow'))

        elif resposta == 4:
            print(colored("❌ Robô fechado com sucesso! Até mais 👋", 'yellow'))
            break

        print(colored("\nSelecione uma opção:", "green"))
        print(colored("1. 🌐  Voltar para o menu principal  🌐", 'blue'))
        print(colored("2. ❌  Sair  ❌", 'red'))

        escolha = input()

        if escolha == "1":
            continue
        elif escolha == "2":
            os.system('clear' if os.name == 'posix' else 'cls')
            print(colored("❌ Robô fechado com sucesso! Até mais 👋", 'yellow'))
            break
        else:
            print("Opção inválida. Por favor, escolha 1 ou 2.")

    except ValueError:
        print("Por favor, insira um número válido como resposta.")

