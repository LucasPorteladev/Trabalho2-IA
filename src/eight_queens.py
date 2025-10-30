# src/eight_queens.py
# Representação: board[c] = linha (0..7) da rainha na coluna c (0..7)

from typing import List, Iterable, Tuple
import random

Board = List[int]
Move = Tuple[int, int]  # (coluna, nova_linha)
N = 8

def initial_board() -> Board:
    #Gera um tabuleiro inicial aleatório
    return [random.randint(0, N - 1) for _ in range(N)]

def conflicts(board: Board) -> int:
    #Calcula o número de pares de rainhas em conflito
    count = 0
    for c1 in range(N):
        for c2 in range(c1 + 1, N):
            r1, r2 = board[c1], board[c2]
            if r1 == r2 or abs(r1 - r2) == abs(c1 - c2):
                count += 1
    return count

def neighbors(board: Board) -> Iterable[Move]:
    #Gera movimentos vizinhos: mover cada rainha para qualquer outra linha
    for c in range(N):
        current = board[c]
        for r in range(N):
            if r != current:
                yield (c, r)

def apply(board: Board, mv: Move) -> Board:
    #Aplica um movimento (coluna, nova_linha) e retorna um novo tabuleiro
    c, r = mv
    newb = board.copy()
    newb[c] = r
    return newb

def print_board(board: Board):
    #Imprime o tabuleiro de forma legível
    for row in range(N):
        line = ""
        for col in range(N):
            line += "Q " if board[col] == row else ". "
        print(line)
