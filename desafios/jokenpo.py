player_1 = int(input("Escolha um valor para o jogador 1 (1: Pedra, 2: Papel, 3: Tesoura): "))
player_2 = int(input("Escolha um valor para o jogador 2 (1: Pedra, 2: Papel, 3: Tesoura): "))

if 1 <= player_1 <= 3 and 1 <= player_2 <= 3:
    if player_1 == player_2:
        print("EMPATE")
    elif (player_1 == 1 and (player_2 == 3)) or \
         (player_1 == 2 and (player_2 == 1)) or \
         (player_1 == 3 and (player_2 == 2)):
        print("Jogador 1 ganha!")
    else:
        print("Jogador 2 ganha!")
else:
    print("Escolha inválida. Certifique-se de escolher um valor entre 1 e 3.")