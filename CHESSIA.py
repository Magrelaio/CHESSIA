import chess
from ia_beta import motor_de_xadrez_simples

def jogar_xadrez():
    tabuleiro = chess.Board()
    legais = list(tabuleiro.legal_moves)
    print(legais)

    
    while not tabuleiro.is_game_over():
        print(tabuleiro)
        if tabuleiro.turn == chess.WHITE:
            movimento = input("Sua jogada: ")
        else:
            movimento = motor_de_xadrez_simples(tabuleiro)
        tabuleiro.push_san(movimento)
    
    print("Fim do jogo")
    print("Resultado: " + tabuleiro.result())

# Iniciar o jogo
jogar_xadrez()
