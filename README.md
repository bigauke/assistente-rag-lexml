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

## Equipe e responsabilidades

* Engenharia e Infra: Daniel Linhares e Camila
* Dados e Ingestão (XML): Nathalia
* Baselines e LLM: Gisele

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


# Especificação do Projeto: Assistente de Consulta à Legislação Brasileira via RAG

## 1. Resumo do Entendimento
*   **O que será construído:** Um assistente RAG conversacional que responde sobre legislação federal (CLT, Código Civil, Marco Civil) cruzando a "lei seca" (subconjunto de ~500 leis do LexML) com a Jurisprudência/Súmulas dos tribunais superiores (STF, STJ, TST).
*   **Por que existe:** Para aplicar na prática técnicas de Machine Learning e Eng. de Dados, testando diferentes estratégias de *chunking* e utilizando *LLM-as-a-judge* para avaliar fidelidade e relevância.
*   **Para quem é:** Profissionais do Direito (advogados, juízes, promotores), exigindo jargão técnico, exatidão e referências cruzadas precisas (Lei + Jurisprudência).
*   **Não-objetivos explícitos:** Não tem o objetivo de atender o público leigo (linguagem simplificada) e não será construído para alta escalabilidade (milhares de acessos simultâneos), focando na qualidade da recuperação (*retrieval*).

## 2. Premissas (Assumptions)
1. **Desempenho:** Respostas entre 5 e 15 segundos são aceitáveis para a PoC.
2. **Ambiente:** O sistema rodará em um ambiente de PoC acadêmico (Google Colab, máquina local com Ollama ou deploy simples no HuggingFace/Streamlit).
3. **Privacidade:** Os avaliadores não inserirão dados reais/sigilosos de clientes no prompt.
4. **Dados Adicionais:** Assumimos que, além do corpus LexML fornecido, o grupo providenciará (via scraping ou base aberta) um corpus adicional em texto/PDF das Súmulas e julgados principais.

## 3. Registro de Decisões (Decision Log)
*   **Decisão 1:** Foco estrito em profissionais do Direito.
    *   *Alternativas:* Focar em estudantes ou público leigo.
    *   *Por que:* Advogados exigem precisão (citações exatas), o que aumenta a barra de exigência técnica do RAG, servindo perfeitamente para validar as estratégias de *chunking* e evitar alucinações.
*   **Decisão 2:** Inclusão de Jurisprudência além da Lei Seca.
    *   *Alternativas:* Usar apenas as ~500 leis.
    *   *Por que:* A lei isolada raramente resolve o problema prático de um advogado; o cruzamento com STF/STJ/TST enriquece o desafio de Engenharia de Dados e modelagem semântica.
*   **Decisão 3:** Abordagem de Multi-Vector Retrieval (Parent-Child) via ChromaDB com GPT-4o-mini.
    *   *Alternativas:* Naive FAISS index ou Hybrid Keyword Search.
    *   *Por que:* Evita a perda de contexto jurídico que ocorre ao cortar artigos no meio (naive chunking) e provê melhor capacidade de filtragem por metadados que o FAISS puro.

---

## 4. Especificação Final (Design)

### 4.1 Definição do Problema
*   **Contexto e Justificativa:** Profissionais do Direito gastam muito tempo cruzando a legislação com o entendimento dos tribunais. Modelos de linguagem genéricos costumam "alucinar" números de artigos ou criar leis inexistentes, gerando grave risco profissional.
*   **Escopo Delimitado:** O projeto desenvolverá um assistente conversacional ancorado na verdade terrestre (RAG), focado em responder perguntas técnicas usando um subconjunto temático de ~500 leis federais (CLT, Código Civil, Marco Civil) e jurisprudências associadas.

### 4.2 Dados e Pré-processamento
*   **Origem e Licença:** Base da "lei seca" extraída do LexML Brasil (corpus federal, licença aberta, XML/PDF). A jurisprudência será coletada de portais abertos dos tribunais superiores.
*   **Volume e Riscos:** Volume moderado focado no subset de 500 leis. Os riscos englobam falhas de OCR/parsing em PDFs antigos e a necessidade de separar o texto legislativo de ementas complexas.
*   **Estratégia de Pré-processamento:** Limpeza de ruídos (cabeçalhos, números de página), parsing estruturado do XML para manter a hierarquia legal (Artigo, Parágrafo, Inciso) e enriquecimento com metadados cruciais (ano, tribunal, tipo de lei).

### 4.3 Metodologia
*   **Abordagem Técnica:** O sistema empregará a arquitetura *Retrieval-Augmented Generation* (RAG). Usaremos o ChromaDB para armazenamento vetorial, embeddings `intfloat/multilingual-e5-large` otimizados para português e GPT-4o-mini para a geração textual fluida e técnica.
*   **Diferencial e Testes:** Implementação do padrão de *chunking* *Parent-Child* (Multi-Vector Retrieval), comparando o desempenho do "chunking estrutural" (quebrando logicamente nas fronteiras dos incisos) contra o "chunking ingênuo" (quebrando a cada X tokens). 
*   **Baseline:** O desempenho será contraposto a um sistema clássico de busca lexical por palavras-chave.
*   **Protocolo de Validação:** Avaliação automatizada via pipeline de *LLM-as-a-judge* pontuando Fidelidade (o texto gerado está no contexto?) e Relevância (a resposta atende a pergunta?).

### 4.4 Cronograma
*   **Fase 1 (Até 29/Maio):** Obtenção/Limpeza do subset de leis e jurisprudência. Setup do ambiente e apresentação da "Pré-especificação" para aprovação do instrutor.
*   **Fase 2 (Junho):** Implementação da indexação (ChromaDB + embeddings) testando as abordagens de chunking. Configuração da busca baseline.
*   **Fase 3 (Até 30/Junho):** Documentação técnica final consolidando os resultados para a **Entrega 1**.
*   **Fase 4 (Pós-Entrega 1):** Desenvolvimento do módulo *LLM-as-a-judge*, rodadas de teste final do RAG e refinamento do prompt do gerador.

### 4.5 Métricas de Sucesso
*   **Indicador 1 (Eficácia Geral):** Porcentagem de respostas corretas em um benchmark manual focado em profissionais jurídicos. *Mínimo Aceitável: ≥ 70%.*
*   **Indicador 2 (Fidelidade / LLM-as-a-judge):** Taxa de respostas onde o modelo baseou-se estritamente no documento recuperado, sem inventar dispositivos. *Mínimo Aceitável: ≥ 85%.*
*   **Indicador 3 (Recall da Recuperação):** A norma/súmula mais pertinente para responder a questão deve figurar no Top-3 dos resultados recuperados pelo vetor. *Mínimo Aceitável: ≥ 75%.*

