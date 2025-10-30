# src/hill_climbing.py
import time
import random
from typing import Optional
from eight_queens import initial_board, conflicts, neighbors, apply


def hill_climbing(max_restarts=100, max_side_moves=50, allow_side_moves=True, start_board: Optional[list] = None):
    start_time = time.time()
    best_board = None
    best_conflicts = float("inf")
    restarts_done = 0
    total_conflicts_evaluated = 0  # NOVO

    for restart in range(max_restarts + 1):
        # Usa o tabuleiro inicial fornecido apenas na primeira execução
        board = start_board.copy() if (restart == 0 and start_board is not None) else initial_board()
        current_conflicts = conflicts(board)
        total_conflicts_evaluated += 1
        side_moves = 0

        while True:
            moves = list(neighbors(board))
            improved_moves = []
            equal_moves = []

            # Avalia todos os vizinhos
            for mv in moves:
                new_board = apply(board, mv)
                cf = conflicts(new_board)
                total_conflicts_evaluated += 1  # Contabiliza cada avaliação

                if cf < current_conflicts:
                    improved_moves.append((new_board, cf))
                elif allow_side_moves and cf == current_conflicts:
                    equal_moves.append((new_board, cf))

            # --- Caso 1: Há movimentos melhores ---
            if improved_moves:
                board, current_conflicts = random.choice(improved_moves)
                side_moves = 0  # Zera contagem de laterais

            # --- Caso 2: Nenhum melhor, mas laterais permitidos ---
            elif equal_moves and allow_side_moves and side_moves < max_side_moves:
                board, current_conflicts = random.choice(equal_moves)
                side_moves += 1
                continue

            # --- Caso 3: Nenhum movimento útil ---
            else:
                break

            # --- Se encontrou solução perfeita ---
            if current_conflicts == 0:
                elapsed = time.time() - start_time
                return board, current_conflicts, restart, elapsed, True, total_conflicts_evaluated

        # Atualiza melhor global
        if current_conflicts < best_conflicts:
            best_conflicts = current_conflicts
            best_board = board.copy()

        restarts_done += 1

    elapsed = time.time() - start_time
    success = best_conflicts == 0
    return best_board, best_conflicts, restarts_done, elapsed, success, total_conflicts_evaluated
