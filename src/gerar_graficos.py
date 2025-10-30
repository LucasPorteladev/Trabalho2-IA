# src/gerar_graficos.py

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import sys

# Nome padrão do CSV (relativo à pasta src)
DEFAULT_CSV = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "results", "results.csv"))
# Pasta de saída (fora da pasta src)
OUT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "results"))


def annotate_bars(ax, bars, fmt="{:.2f}", offset=0.01):
    for bar in bars:
        h = bar.get_height()
        ax.annotate(fmt.format(h),
                    xy=(bar.get_x() + bar.get_width() / 2, h),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha="center", va="bottom", fontsize=8)


def gerar_graficos(caminho_csv: str = None):
    caminho_csv = caminho_csv or DEFAULT_CSV

    # Verifica existência do CSV
    if not os.path.isfile(caminho_csv):
        msg = (
            f"Arquivo CSV não encontrado: {caminho_csv}\n\n"
            "Por favor, coloque o CSV de resultados em:\n"
            f"  {os.path.dirname(caminho_csv)}\n\n"
            "O CSV esperado deve conter, no mínimo, as colunas:\n"
            "  'Algoritmo', 'Execucao', 'Conflitos', 'Iteracoes', 'Tempo', 'Sucesso'\n\n"
            "Exemplo de execução (a partir de trabalho2/src):\n"
            "  python gerar_graficos.py ../results/results.csv\n"
        )
        raise FileNotFoundError(msg)

    # Cria pasta de saída (../results)
    os.makedirs(OUT_DIR, exist_ok=True)

    # Lê o CSV
    df = pd.read_csv(caminho_csv)

    # Verifica colunas necessárias
    colunas_necessarias = {'Algoritmo', 'Conflitos', 'Iteracoes', 'Tempo', 'Sucesso'}
    if not colunas_necessarias.issubset(df.columns):
        raise ValueError(f"O CSV deve conter as colunas: {colunas_necessarias}. Colunas atuais: {set(df.columns)}")

    # Agrupa dados por tipo de algoritmo e calcula métricas
    grupo = df.groupby("Algoritmo").agg({
        "Conflitos": ["mean", "std"],
        "Iteracoes": ["mean", "std"],
        "Tempo": ["mean", "std"],
        "Sucesso": "mean"
    }).reset_index()

    # Renomeia colunas para fácil acesso
    grupo.columns = ["Algoritmo", "Conflitos_medio", "Conflitos_std",
                     "Iteracoes_medias", "Iteracoes_std",
                     "Tempo_medio", "Tempo_std", "Taxa_sucesso"]

    # ---- 1. Taxa de sucesso (%) ----
    plt.figure(figsize=(8, 5))
    bars = plt.bar(grupo["Algoritmo"], grupo["Taxa_sucesso"] * 100, edgecolor="black")
    plt.title("Taxa de Sucesso (%) por Algoritmo", fontsize=14)
    plt.ylabel("Taxa de Sucesso (%)")
    plt.xticks(rotation=20)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    annotate_bars(plt.gca(), bars, fmt="{:.1f}", offset=0.01)
    plt.tight_layout()
    path = os.path.join(OUT_DIR, "taxa_sucesso.png")
    plt.savefig(path, dpi=300)
    plt.close()

    # ---- 2. Tempo médio ----
    plt.figure(figsize=(8, 5))
    bars = plt.bar(grupo["Algoritmo"], grupo["Tempo_medio"], edgecolor="black")
    plt.title("Tempo Médio de Execução por Algoritmo", fontsize=14)
    plt.ylabel("Tempo (s)")
    plt.xticks(rotation=20)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    annotate_bars(plt.gca(), bars, fmt="{:.4f}")
    plt.tight_layout()
    path = os.path.join(OUT_DIR, "tempo_medio.png")
    plt.savefig(path, dpi=300)
    plt.close()

    # ---- 3. Conflitos médios ----
    plt.figure(figsize=(8, 5))
    bars = plt.bar(grupo["Algoritmo"], grupo["Conflitos_medio"], edgecolor="black")
    plt.title("Número Médio de Conflitos por Algoritmo", fontsize=14)
    plt.ylabel("Conflitos Médios")
    plt.xticks(rotation=20)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    annotate_bars(plt.gca(), bars, fmt="{:.2f}")
    plt.tight_layout()
    path = os.path.join(OUT_DIR, "conflitos_medios.png")
    plt.savefig(path, dpi=300)
    plt.close()

    # ---- 4. Iterações médias ----
    plt.figure(figsize=(8, 5))
    bars = plt.bar(grupo["Algoritmo"], grupo["Iteracoes_medias"], edgecolor="black")
    plt.title("Número Médio de Iterações por Algoritmo", fontsize=14)
    plt.ylabel("Iterações Médias")
    plt.xticks(rotation=20)
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    annotate_bars(plt.gca(), bars, fmt="{:.1f}")
    plt.tight_layout()
    path = os.path.join(OUT_DIR, "iteracoes_medias.png")
    plt.savefig(path, dpi=300)
    plt.close()

    print(f"\n Gráficos gerados em: {OUT_DIR}")
    print("Arquivos:")
    for nome in [
        "taxa_sucesso.png",
        "tempo_medio.png",
        "conflitos_medios.png",
        "iteracoes_medias.png",
        "comparativo_metricas.png",
    ]:
        print(" -", os.path.join(OUT_DIR, nome))


if __name__ == "__main__":
    csv_path = sys.argv[1] if len(sys.argv) > 1 else None
    try:
        gerar_graficos(csv_path)
    except Exception as e:
        print("Erro:", e)
        sys.exit(1)
