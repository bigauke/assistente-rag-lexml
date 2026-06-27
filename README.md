# Assistente RAG LexML

Este repositório contém a infraestrutura de engenharia de dados e o motor cognitivo RAG (Retrieval-Augmented Generation) desenvolvido para estruturar consultas inteligentes em documentos legislativos. O sistema utiliza Processamento de Linguagem Natural (NLP) e bancos de dados vetoriais para buscas semânticas de alta precisão.

---

## 🏗️ Arquitetura e Engenharia

A fundação do projeto segue padrões rigorosos de desenvolvimento e gestão de dados:

* **Gestão de Dependências:** Instalação e isolamento de ambiente otimizados com `uv` (Python 3.12).
* **Estruturação Modular:** Encapsulamento da regra de negócio no pacote `assistente_rag_lexml`.
* **Data Pipeline:** Diretórios segmentados para o ciclo de vida dos dados (`data/raw`, `data/processed`, `models` e `notebooks`).
* **Motor Vetorial:** Indexação semântica validada com `FAISS` e embeddings do `HuggingFace` (`vector_store.py`).
* **Ingestão ETL:** Pipeline automatizado para extração e limpeza de textos a partir de documentos XML (`data_ingestion.py`).

---

## ✅ Status de Validação

**Última validação:** Maio de 2026
Infraestrutura homologada com sucesso:
* **Ingestão:** Identificação e processamento íntegro de arquivos XML mapeados em `data/raw` via `main.py`.
* **Indexação Vetorial:** Download automático do modelo `all-MiniLM-L6-v2` e geração do índice FAISS.
* **Busca Semântica:** Recuperação de contexto (retrieval) com alta precisão e relevância estrutural.

---

## ⚙️ Guia de Instalação e Configuração

Siga o fluxo abaixo utilizando o **Git Bash** (ou terminal equivalente).

**1. Clonar o repositório**
```bash
git clone [https://github.com/saimomgozn-collab/assistente-rag-hacarthon.git](https://github.com/saimomgozn-collab/assistente-rag-hacarthon.git)
cd assistente-rag-hacarthon
```

**2. Instalar o gestor de pacotes (`uv`)**
Via PowerShell (Windows):
```powershell
powershell -ExecutionPolicy Bypass -Command "irm [https://astral.sh/uv/install.ps1](https://astral.sh/uv/install.ps1) | iex"
```

**3. Sincronizar dependências**
```bash
uv sync
```

**4. Ativar o ambiente virtual**
```bash
source .venv/Scripts/activate
```

**5. Configurar variáveis de ambiente**
```bash
cp .env.example .env
```

---

## 👥 Equipe e Responsabilidades

Cada membro possui uma área de atuação definida para garantir a agilidade das entregas e evitar sobreposição de tarefas:

| Frente de Atuação | Responsáveis | Escopo Principal |
| :--- | :--- | :--- |
| **Engenharia & Infra** | Daniel Linhares | Manutenção do motor RAG, validação de ambiente e revisão de Pull Requests. |
| **Dados & Ingestão (XML)** | Nathalia, Camila e Saimom | Coleta, limpeza e estruturação dos documentos oficiais na pipeline `data/raw`. |
| **Baselines & LLM** | Gisele e Stanley | Elaboração de notebooks de teste, refinamento de prompts e avaliação de métricas. |

---

## 🚀 Guia de Colaboração (Git Flow)

Para garantir a integridade do repositório, adotamos um fluxo de versionamento estruturado:

| Etapa | Comando | Descrição |
| :--- | :--- | :--- |
| **1. Sync** | `git checkout main && git pull origin main` | Atualiza seu ambiente local com a versão mais recente. |
| **2. Branch** | `git checkout -b feat/nome-da-tarefa` | Isola seu desenvolvimento em uma nova branch. |
| **3. Commit** | `git commit -m "feat: adiciona extrator XML"` | Registra alterações utilizando prefixos padrão (`feat:`, `fix:`, `docs:`). |
| **4. Push** | `git push origin feat/nome-da-tarefa` | Envia suas alterações para o repositório remoto. |
| **5. PR** | *Ação via GitHub* | Abre um Pull Request solicitando Code Review e integração. |

### Padrões de Ambiente

* **Gestão:** Uso obrigatório do `uv` para assegurar isolamento idêntico entre sistemas operacionais.
* **Execução:** Utilize `uv run python main.py` para garantir o carregamento correto das bibliotecas de IA.
* **Dados Brutos:** Qualquer novo dump de dados deve ser alocado exclusivamente no diretório `data/raw`.