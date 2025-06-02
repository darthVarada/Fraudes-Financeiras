# 💼 Projeto: Detecção de Fraudes em Transações Financeiras

Este projeto tem como objetivo identificar transações fraudulentas em um grande volume de dados financeiros utilizando técnicas de Machine Learning e análise exploratória.

---

## 📦 Estrutura dos Arquivos

| Arquivo / Pasta     | Descrição |
|---------------------|-----------|
| `.venv/`            | Ambiente virtual Python (gerado localmente com `uv sync`) |
| `.gitignore`        | Padrões de arquivos ignorados pelo Git |
| `.python-version`   | Versão do Python usada no projeto |
| `estudo.ipynb`      | Notebook principal com a análise e modelagem |
| `LICENSE`           | Licença do projeto |
| `main.py`           | Script Python principal com execução de modelo |
| `pyproject.toml`    | Configurações do ambiente e dependências |
| `uv.lock`           | Lockfile de dependências (não editar manualmente) |
| `README.md`         | Este arquivo com instruções do projeto |

---

## 🚀 Como executar o projeto com `uv`

Este projeto usa o [uv](https://docs.astral.sh/uv/) para gerenciar ambientes e dependências.

### 1. Instale o `uv` (se ainda não tiver)

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Ou via pipx:

```bash
pipx install uv
```

### 2. Sincronize o ambiente com o lockfile

> Isso cria o ambiente virtual `.venv/` e instala todas as dependências automaticamente.

```bash
uv sync
```

### 3. Ative o ambiente virtual

```bash
# Linux/macOS
source .venv/bin/activate

# Windows
.venv\Scripts\activate
```

---

## 📊 Execução dos códigos

- A análise completa está em `estudo.ipynb` (abra com Jupyter ou VS Code).
- Você também pode executar diretamente o script `main.py`.

---

## 🛠 Requisitos principais

- Python 3.10+
- pandas, numpy, matplotlib, seaborn, scikit-learn, tqdm, jupyter

---

## 👥 Integrantes

- Nome 1 – [LinkedIn](#)
- Nome 2 – [LinkedIn](#)

---

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.
