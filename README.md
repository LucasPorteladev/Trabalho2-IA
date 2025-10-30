# Repositório - Trabalho 1 Inteligência Artificial

Este repositório contém o primeiro trabalho prático desenvolvido para a disciplina G05IART0.02 - Inteligência Artificial, ministrada pelo Prof. Tiago Alves de Oliveira, no Centro Federal de Educação Tecnológica de Minas Gerais (CEFET-MG), Campus V.

## Estrutura do Repositório
```bash
trabalho2/
├─ src/
│  ├─ eight_queens.py  
│  ├─ hill_climbing.py  
│  ├─ gerar_graficos.py   
│  ├─ lateral.py           
│  └─ reinicio.py         
│
├─ results/                
│  ├─ lateral.txt          
│  ├─ reinicio.txt         
│  ├─ results.csv         
│  ├─ conflitos_medios.png 
│  ├─ iteracoes_medias.png 
│  ├─ taxa_sucesso.png     
│  └─ tempo_medio.png    
│
├─ requirements.txt       
└─ README.md              
```

## Instalação

1. Clone o repositório:
```bash
#usando HTTPS
git clone <https://github.com/LucasPorteladev/Trabalho2-IA.git>
```
2. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Como executar os códigos

1. Rodar as execuções com o algoritmo lateral
```bash
python src/lateral.py
```
Este script executa o algoritmo Hill Climbing com movimentos laterais, realizando múltiplas execuções e salvando os resultados em results/lateral.txt.

2. Rodar as execuções com o algoritmo de reinício
```bash
python src/reinicio.py
```
Este script executa o algoritmo Hill Climbing com reinícios aleatórios, armazenando os resultados em results/reinicio.txt.

3. Gerar gráficos comparativos
```bash
python src/gerar_graficos.py
```
Este script cria gráficos que comparam o desempenho entre as diferentes variações do algoritmo, com base nos resultados obtidos.

## Resultados Obtidos

Os resultados detalhados das execuções e comparações de desempenho podem ser consultados no PDF abaixo:

👉 [**Relatório de Resultados (PDF)**](./trabalho2_lucasportela.pdf)

---

# Ambiente de Execução

| **Máquina**         | **Processador**                     | **Memória RAM** | **Sistema Operacional** |
|---------------------|-------------------------------------|-----------------|--------------------------|
| Acer Nitro V15      | 13th Intel(R) Core(TM) i7-13620H    | 32 GB  5200MHz  | Windows 11             |

--- 

##  Autor

*Lucas Cerqueira Portela* — *Estudante de Engenharia de Computação @ CEFET-MG*  
