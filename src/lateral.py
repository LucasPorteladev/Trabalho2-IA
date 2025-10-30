# src/lateral.py
import time
import os
import csv
from hill_climbing import hill_climbing
from eight_queens import print_board, initial_board

RESULTS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "results"))
CSV_PATH = os.path.join(RESULTS_DIR, "results.csv")

def salvar_csv(algoritmo, execucao, conflitos, iteracoes, tempo, sucesso):
    """Salva (ou adiciona) resultados no CSV."""
    os.makedirs(RESULTS_DIR, exist_ok=True)
    cabecalho = ["Algoritmo", "Execucao", "Conflitos", "Iteracoes", "Tempo", "Sucesso"]
    existe = os.path.exists(CSV_PATH)

    with open(CSV_PATH, "a", newline="") as f:
        writer = csv.writer(f)
        if not existe:
            writer.writerow(cabecalho)
        writer.writerow([algoritmo, execucao, conflitos, iteracoes, tempo, int(sucesso)])


def main(execucoes=100):
    saida_path = os.path.join(RESULTS_DIR, "lateral.txt")
    os.makedirs(RESULTS_DIR, exist_ok=True)

    tempos, conflitos_totais, iteracoes_totais, sucessos = [], [], [], []

    with open(saida_path, "w") as f:
        for i in range(1, execucoes + 1):
            # --- Gera tabuleiro inicial e executa Hill Climbing ---
            initial = initial_board()

            inicio = time.time()  # 🔧 Correção: substituído time.tempo_exec() por time.time()
            board, conflito_final, reinicios, tempo_exec, sucesso, conflito = hill_climbing(
                max_restarts=0, allow_side_moves=True, start_board=initial
            )
            fim = time.time()
            tempo_exec = fim - inicio  # Tempo total da execução

            # --- Estatísticas ---
            tempos.append(tempo_exec)
            conflitos_totais.append(conflito)
            iteracoes_totais.append(reinicios)
            sucessos.append(int(sucesso))

            # --- Impressão na tela ---
            print(f"\nExecução {i}\n")
            print("TABULEIRO INICIAL:")
            print_board(initial)
            print("\nTABULEIRO FINAL:")
            print_board(board)
            print(f"\nTEMPO: {tempo_exec:.4f}  CONFLITO: {conflito}\n")

            # --- Escrita no arquivo ---
            f.write(f"Execução {i}\n\n")

            f.write("TABULEIRO INICIAL:\n")
            for row in range(8):
                linha = ""
                for col in range(8):
                    linha += "Q " if initial[col] == row else ". "
                f.write(linha + "\n")

            f.write("\nTABULEIRO FINAL:\n")
            for row in range(8):
                linha = ""
                for col in range(8):
                    linha += "Q " if board[col] == row else ". "
                f.write(linha + "\n")

            f.write(f"\nTEMPO: {tempo_exec:.4f}  CONFLITO: {conflito}\n\n")

            # --- Salva no CSV ---
            salvar_csv("Lateral", i, conflito, reinicios, tempo_exec, sucesso)

        # --- Cálculo de médias ---
        media_tempo = sum(tempos) / len(tempos)
        media_conflitos = sum(conflitos_totais) / len(conflitos_totais)
        taxa_sucesso = sum(sucessos) / len(sucessos) * 100

        print(f"\n--- MÉDIAS ---")
        print(f"Tempo médio: {media_tempo:.4f}s")
        print(f"Conflitos médios: {media_conflitos:.2f}")
        print(f"Taxa de sucesso: {taxa_sucesso:.1f}%")

        f.write(f"\n--- MÉDIAS ---\n")
        f.write(f"Tempo médio: {media_tempo:.4f}s\n")
        f.write(f"Conflitos médios: {media_conflitos:.2f}\n")
        f.write(f"Taxa de sucesso: {taxa_sucesso:.1f}%\n")


if __name__ == "__main__":
    main()
