from assistente_rag_lexml.data_ingestion import load_lexml_documents
from assistente_rag_lexml.vector_store import create_or_load_vector_store

def main():
    print("🚀 Iniciando o Assistente RAG LexML...")

    # 1. Carregar documentos da pasta correta
    print("📂 Carregando documentos de data/raw...")
    docs = load_lexml_documents("data/raw")
    
    if not docs:
        print("⚠️ Nenhum XML encontrado em data/raw. Adicione arquivos para continuar.")
        return

    # 2. Processar banco vetorial
    print(f"🧠 Indexando {len(docs)} documentos...")
    # O caminho do índice deve apontar para a pasta models na raiz
    vector_store = create_or_load_vector_store(documents=docs, index_path="models/faiss_index")
    
    # 3. Teste rápido
    query = "do que tratam esses documentos?"
    results = vector_store.similarity_search(query, k=1)
    
    print(f"\n✅ Teste concluído. Resultado mais relevante: {results[0].metadata.get('source')}")

if __name__ == "__main__":
    main()