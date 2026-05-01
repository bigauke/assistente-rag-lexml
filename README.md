# Assistente RAG LexML

Este repositório contém a infraestrutura de engenharia e o motor de busca RAG (Retrieval-Augmented Generation) desenvolvido para o projeto de assistência jurídica baseado nos dados do LexML. O sistema permite consultas inteligentes em documentos legislativos utilizando NLP e bancos de dados vetoriais.

---

## O que construímos

A fundação do projeto foi estabelecida seguindo as melhores práticas de mercado:

* **Gestão de Dependências:** Uso do `uv` para instalação rápida de pacotes Python 3.12.
* **Módulo Python:** Estruturação do pacote `assistente_rag_lexml`.
* **Arquitetura de Dados:** Diretórios para o ciclo de vida dos dados: `data/raw`, `data/processed`, `models` e `notebooks`.
* **Banco Vetorial:** Motor de busca validado com `FAISS` e embeddings do `HuggingFace` (`vector_store.py`).
* **ETL Pipeline:** Extração de textos de documentos XML do LexML (`data_ingestion.py`).

---

## ✅ Status da Validação (01/05/2026)

A infraestrutura foi testada e validada com sucesso no ambiente Windows:
- **Teste de Ingestão:** O script `main.py` identificou e processou arquivos XML em `data/raw`.
- **Indexação Vetorial:** O modelo `all-MiniLM-L6-v2` foi baixado e gerou o índice FAISS corretamente.
- **Busca Semântica:** O sistema retornou resultados relevantes para perguntas de teste.

---

## Guia de instalação e configuração

Siga os passos abaixo utilizando o **Git Bash**.

1. Clonar o repositório

```bash
git clone https://github.com/bigauke/assistente-rag-lexml.git
cd assistente-rag-lexml
```

2. Instalar o `uv`

Instale o gestor de pacotes via PowerShell:

```powershell
powershell -ExecutionPolicy Bypass -Command "irm https://astral.sh/uv/install.ps1 | iex"
```

3. Sincronizar dependências

```bash
uv sync
```

4. Ativar o ambiente virtual

No Git Bash:

```bash
source .venv/Scripts/activate
```

5. Configurar variáveis de ambiente

```bash
cp .env.example .env
```

## Equipe e responsabilidades

* Engenharia e Infra: Daniel Linhares e Camila
* Dados e Ingestão (XML): Nathalia
* Baselines e LLM: Gisele
