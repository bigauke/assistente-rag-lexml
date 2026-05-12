# Assistente RAG LexML

Este repositório contém a infraestrutura de engenharia e o motor de busca RAG (Retrieval-Augmented Generation) desenvolvido para o projeto de assistência jurídica baseado nos dados do LexML. O sistema permite consultas inteligentes em documentos legislativos utilizando NLP e bancos de dados vetoriais.

---

## O que construímos

A fundação do projeto foi estabelecida seguindo as melhores práticas de mercado:

* **Gestão de dependências:** uso do `uv` para instalação rápida de pacotes Python 3.12.
* **Módulo Python:** estruturação do pacote `assistente_rag_lexml`.
* **Arquitetura de dados:** diretórios para o ciclo de vida dos dados: `data/raw`, `data/processed`, `models` e `notebooks`.
* **Banco vetorial:** motor de busca validado com `FAISS` e embeddings do `HuggingFace` (`vector_store.py`).
* **ETL pipeline:** extração de textos de documentos XML do LexML (`data_ingestion.py`).

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

## 👥 Equipe e Responsabilidades

| Integrante | Papel Principal | Atribuições Técnicas |
| :--- | :--- | :--- |
| **Daniel Linhares** | Líder de Equipe, Engenharia & Comunicação | Coordenação geral, infraestrutura de pipeline e narrativa técnica. |
| **Nathalia Gomes** | Líder de Dados & Comunicação | ]Aquisição/curadoria do dataset LexML, EDA e suporte na defesa oral. |
| **Gisele Fonseca** | Líder de Modelagem | Treinamento do RAG, implementação de baselines e comparação de modelos. |
| **Camila Soares** | Líder de Engenharia | Reprodutibilidade do ambiente (Docker/uv) e integridade do pipeline. |
| **Saimom Goz Siebem** | Líder de Avaliação & Comunicação | [cite_start]Métricas de sucesso, análise de erros/alucinação e defesa técnica. |
| **Stanley de Oliveira Souza** | Líder de Documentação | Redação da proposta formal, manutenção do README e controle de versão. |

---

## 🚀 Guia de colaboração profissional: Projeto LexML

Para garantirmos a integridade do código e a agilidade nas entregas, adotaremos o seguinte fluxo de trabalho.

### 1. Divisão de frentes (squad)

Cada membro possui uma área de atuação clara para evitar sobreposição de tarefas e conflitos de código:

| Membro | Frente de atuação | Responsabilidade principal |
|---|---|---|
| Daniel Linhares | Engenharia & Infra | Manutenção do motor RAG, validação de ambiente e revisão de Pull Requests. |
| Nathalia, Camila & Saimon | Dados & Ingestão | Coleta, limpeza e estruturação dos XMLs oficiais do LexML na pasta `data/raw`. |
| Gisele & Stanley | Baselines & LLM | Criação de notebooks de teste, refino de prompts e avaliação da precisão das respostas. |

### 2. Fluxo de trabalho no Git (Git Flow profissional)

| Passo | Ação | Comando / Descrição |
|---|---|---|
| 1. Sync | Atualizar sua máquina local | `git checkout main` seguido de `git pull origin main` |
| 2. Branch | Criar ramo para sua tarefa | `git checkout -b feat/nome-da-sua-tarefa` |
| 3. Commit | Registrar alterações | Use prefixos: `feat:` (dados/funções), `fix:` (correções) ou `docs:` |
| 4. Push | Enviar para o servidor | `git push origin nome-da-sua-branch` |
| 5. PR | Integrar ao projeto | Abrir um Pull Request no GitHub para revisão do Daniel. |

### 3. Padrões de ambiente e execução

| Ferramenta | Padrão adotado | Motivo |
|---|---|---|
| Gestor | `uv` | Garante velocidade e isolamento idêntico entre Windows/Linux. |
| Execução | `uv run python main.py` | Garante que todas as bibliotecas de IA sejam carregadas corretamente. |
| Dados | `data/raw` | Local obrigatório para despejo de arquivos XML brutos. |
