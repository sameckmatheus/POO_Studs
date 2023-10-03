import random

# Dicionário que mapeia as opções do jogo
jogadas = {
    'pedra': ['tesoura', 'lagarto'],
    'papel': ['pedra', 'Spock'],
    'tesoura': ['papel', 'lagarto'],
    'lagarto': ['Spock', 'papel'],
    'Spock': ['tesoura', 'pedra']
}


# Função para determinar o vencedor
def determinar_vencedor(jogador, computador):
    if jogador == computador:
        return "Empate!"
    elif computador in jogadas[jogador]:
        return "Você venceu!"
    else:
        return "O computador venceu!"


# Função principal do jogo
def jogar_pedra_papel_tesoura_lagarto_spock():
    print("Bem-vindo ao jogo Pedra, Papel, Tesoura, Lagarto, Spock!")
    while True:
        jogador = input("Escolha sua jogada (pedra, papel, tesoura, lagarto, Spock): ").lower()
        if jogador not in jogadas:
            print("Escolha inválida. Tente novamente.")
            continue

        computador = random.choice(list(jogadas.keys()))
        print(f"O computador escolheu: {computador}")

        resultado = determinar_vencedor(jogador, computador)
        print(resultado)

        jogar_novamente = input("Deseja jogar novamente? (sim/não): ").lower()
        if jogar_novamente != 'sim':
            break


if __name__ == "__main__":
    jogar_pedra_papel_tesoura_lagarto_spock()
