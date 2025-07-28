# PCHM - Coleta de Resíduos com Heurísticas em Python

Este projeto implementa heurísticas adaptadas ao Problema do Caminho Hamiltoniano Mínimo (PCHM) para otimização de rotas de coleta de resíduos sólidos na cidade de Quixadá-CE. As rotas são geradas com base em dados reais e distâncias oficiais obtidas via Google Distance Matrix.

## 📁 Estrutura do Projeto

- `main.py` — Arquivo principal para execução dos algoritmos.
- `cheapest_insertion.py` — Implementação da heurística da Aresta Mais Barata.
- `vizinho_mais_proximo.py` — Implementação da heurística do Vizinho Mais Próximo.
- `utils.py` — Funções auxiliares.
- `img_rotas_via_kepler/` — Imagens das rotas geradas via [kepler.gl](https://kepler.gl).
- `csv_rotas_source/` — Arquivos `.csv` contendo a ligação entre os pontos para visualização no kepler.gl.

---

## ⚙️ Requisitos

- [Python 3.10+](https://www.python.org/downloads/)
- [Anaconda (opcional, mas recomendado)](https://www.anaconda.com/products/distribution)

---

## 🐍 Configuração

1. **Abra o terminal no diretório desejado da sua máquina**

2. **Clone o repositório:**

```bash
git clone https://github.com/jaimegsn/pchm-coleta-residuos.git
```


3. **Entre na Pasta do Projeto:**

```bash
cd pchm-coleta-residuos
```

4. **(Opcional) Crie um ambiente virtual com o Anaconda:**

```bash
conda create -n pchm-env python=3.10

conda activate pchm-env
```

5. **Instale as Dependências:**

```bash
pip install numpy
```

6. **Execute os algoritmos rodando a `main.py`:**

```bash
python main.py
```
