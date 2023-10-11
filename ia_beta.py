import random

def motor_de_xadrez_simples(tabuleiro):
    movimentos_legais = list(tabuleiro.legal_moves)
    movimento_aleatorio = random.choice(movimentos_legais)
    return movimento_aleatorio